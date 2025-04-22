**Example 1: 查询高级设置**

查询高级设置

Input: 

```
tccli dlc DescribeAdvancedStoreLocation --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BucketType": "cos",
        "Enable": 0,
        "HasLakeFs": true,
        "LakeFsStatus": "bind",
        "RequestId": "********-****-****-****-93d48f4f687c",
        "StoreLocation": "cosn://xx/xx/xx"
    }
}
```

