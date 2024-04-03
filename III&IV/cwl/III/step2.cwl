cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/step_2.py"]
hints:
  DockerRequirement:
    dockerPull: lukavasiljevic/cwl-python-env
inputs:
  csv_file:
    type: File
    inputBinding:
      position: 1
  training_ratio:
    type: float
    inputBinding:
      position: 2

outputs:
  output_metrics:
    type: stdout
stdout: metrics.txt