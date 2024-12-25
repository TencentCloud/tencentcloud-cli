**Example 1: 查询集群加密信息**



Input: 

```
tccli cynosdb DescribeClusterTransparentEncryptInfo --cli-unfold-argument  \
    --ClusterId cynosdbmysql-3pd4zrvn
```

Output: 
```
{
    "Response": {
        "KeyId": "9d112608-76f7-11ee-****-525400368ae8",
        "KeyRegion": "ap-guangzhou",
        "RequestId": "c66ada1a-0098-4787-8db8-42be0cee52cd"
    }
}
```

