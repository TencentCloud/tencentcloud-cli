**Example 1: 查询正在一键扫描的镜像扫描taskid**

查询正在一键扫描的镜像扫描taskid

Input: 

```
tccli tcss DescribeAssetImageScanTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskID": "abc",
        "LastScanTime": "abc",
        "Status": "abc",
        "SubStatus": "abc",
        "RequestId": "abc"
    }
}
```

