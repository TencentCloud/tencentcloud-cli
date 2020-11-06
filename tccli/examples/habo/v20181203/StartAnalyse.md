**Example 1: 提交一个样本进行分析**



Input: 

```
tccli habo StartAnalyse --cli-unfold-argument  \
    --Pk authkey \
    --Md5 md5_of_sample \
    --DlUrl http(s)://down.demo.com%2fsample_path
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Info": "success",
        "Data": "",
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6"
    }
}
```

