# Intro

## Azure ML Workspace

workspaces are azure resources. include:

- compute
- notebooks
- pipelines
- data
- experiments
- models

created alongside

- storage account: files by WS + data
- application insights
- key vault
- vm
- container registry

permission: RBAC

edition
- basic (no graphic designer)
- enterprise

## Tools

Azure ML Studio
- designer (no code ML model dev)
- automated ML

Azure ML SDK

Azure ML CLI Extensions

Compute Instances
- choose VM
- store notebooks independently of VMs

VS Code - Azure ML Extension

## Experiments

Azure ML tracks run of experiments

```
...
run = experiment.start_logging()
...
run.complete()
```

- logging metrics. `run.log('name', value)`. You can review them via `RunDetails(run).show()`
- experiment output file. Example: trained models. `run.upload_file(..)`.

**Script as an experiment**. In the script, you can get the context: `run = Rune.get_context()`. To run it, you define:

- RunConfiguration: python environment
- ScriptRunConfig: associates RunConfiguration with script

# Train a ML model

## Estimators

Estimator: encapsulates a run configuration and a script configuration in a single object. Save trained model as pickle in `outputs` folder

```
estimator = Estimator(
  source_directory='experiment',
  entry_script='training.py',
  compute_target='local',
  conda_packages=['scikit-learn']
)
experiment = Experiment(workspace, name='train_experiment')
run = experiment.submit(config=estimator)
```

Framework-specific estimators simplify configurations

```
from azureml.train.sklearn import SKLearn

estimator = SKLearn(
  source_directory='experiment',
  entry_script='training.py',
  compute_target='local'
)
```

## Script parameters

Use `argparse` to read the parameters in a script (eg regularization rate). To pass a parameter to an `Estimator`:

```
estimator = SKLearn(
  source_directory='experiment',
  entry_script='training.py',
  script_params={'--reg_rate': 0.1}
  compute_target='local'
)
```

## Registering models

Once the experiment `Run` has completed, you can retrieve its outputs (eg trained model).

```
run.download_file(name='outputs/models.pkl', output_file_path='model.pkl')
```

Registering a model allows to track multiple versions of a model.

```
model = Model.register(
  workspace=ws,
  model_name='classification_model',
  model_path='model.pkl', #local path
  description='a classification model',
  tags={'dept': 'sales'},
  model_framework=Model.Framework.SCIKITLEARN,
  model_framework_version='0.20.3'
)
```

or register from run:

```
run.register_model(
  ...
  model_path='outputs/model.pkl'
  ...
  )
```
