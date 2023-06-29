**Example 1: 重试任务**

重试任务。

Input: 

```
tccli omics RetryRuns --cli-unfold-argument  \
    --ProjectId prj-aggressive-lime-porcupine-752427 \
    --RunUuids 0118f2ed-43b0-433c-b21c-472fe2bc1766 a273a6f0-ca66-474d-ba04-80f6c73463e9 fc9680c8-35e7-4e82-a5aa-9c506bef6829
```

Output: 
```
{
    "Response": {
        "RequestId": "46520c37-4d28-49e1-a738-01f64ae1b06b"
    }
}
```

