cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["python", "/app/load_data.py"]
hints:
  DockerRequirement:
    dockerPull: lukavasiljevic/cwl-python-env
inputs:
  csv_file:
    type: File
    inputBinding:
      position: 1
  column_name:
    type: string
    inputBinding:
      position: 2

outputs:
  data:
    type: stdout
stdout: data.csv
