cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python"]
hints:
  DockerRequirement:
    dockerPull: lukavasiljevic/cwl-python-env
inputs:
  python_file:
   type: File
   inputBinding:
    position: 1
  csv_file:
    type: File
    inputBinding:
      position: 2
  training_ratio:
    type: float
    inputBinding:
      position: 3

outputs:
  output_metrics:
    type: stdout
stdout: metrics.txt
