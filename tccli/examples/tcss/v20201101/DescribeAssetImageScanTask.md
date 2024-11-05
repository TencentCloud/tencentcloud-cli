**Example 1: 查询正在一键扫描的镜像扫描taskid**

查询正在一键扫描的镜像扫描taskid

Input: 

```
tccli tcss DescribeAssetImageScanTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LastScanTime": "2024-10-11 14:34:15",
        "RequestId": "ebdffbc4-bf83-4e25-bc4c-8ada17cc0481",
        "Status": "END",
        "SubStatus": "Cancel",
        "TaskID": "10000504"
    }
}
```

