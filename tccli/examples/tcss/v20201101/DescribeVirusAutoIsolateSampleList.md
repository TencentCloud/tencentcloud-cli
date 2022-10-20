**Example 1: 查询木马自动隔离样本列表**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "VirusName": "xx",
                "AutoIsolateSwitch": true,
                "MD5": "xx"
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

