**Example 1: 查询木马自动隔离样本列表**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 102,
        "List": [
            {
                "MD5": "61d7d84e979212bed18ed9aa8748defa",
                "VirusName": "virus1",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "AutoIsolateSwitch": true
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

