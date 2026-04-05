**Example 1: 示例**

示例

Input: 

```
tccli wedata GetTraceArtifact --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --MlTraceId 1 \
    --Path 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RawData": "{\"StatusCode\":200,\"ContentType\":\"application/json\",\"ContentDisposition\":\"attachment; filename=1\",\"Headers\":{\"x-mlflow-mock\":\"true\",\"content-disposition\":\"attachment; filename=1\",\"content-type\":\"application/json\"},\"Content\":\"ewogICJ0cmFjZV9pZCI6ICIxIiwKICAic3BhbnMiOiBbCiAgICB7CiAgICAgICJzcGFuX2lkIjogInNwYW4tbW9jay1yb290IiwKICAgICAgIm5hbWUiOiAiYWdlbnQuaW52b2tlIiwKICAgICAgInN0YXR1cyI6ICJPSyIKICAgIH0KICBdLAogICJtb2NrIjogdHJ1ZQp9Cg==\"}"
        },
        "RequestId": "4b4f2846-e967-4620-9d5e-4918263d7d0b"
    }
}
```

