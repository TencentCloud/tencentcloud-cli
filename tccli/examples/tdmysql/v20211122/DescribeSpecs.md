**Example 1: 对等架构返回**



Input: 

```
tccli tdmysql DescribeSpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HybridNodeSpecs": [
            {
                "SpecCode": "1c2g",
                "StorageNodeCpu": 1,
                "StorageNodeMaxDisk": 500,
                "StorageNodeMaxNum": 18,
                "StorageNodeMem": 2,
                "StorageNodeMinDisk": 20,
                "StorageNodeMinNum": 3,
                "StorageType": "CLOUD_HSSD"
            },
            {
                "SpecCode": "2c4g",
                "StorageNodeCpu": 2,
                "StorageNodeMaxDisk": 500,
                "StorageNodeMaxNum": 18,
                "StorageNodeMem": 4,
                "StorageNodeMinDisk": 20,
                "StorageNodeMinNum": 3,
                "StorageType": "CLOUD_HSSD"
            },
            {
                "SpecCode": "4c8g",
                "StorageNodeCpu": 4,
                "StorageNodeMaxDisk": 500,
                "StorageNodeMaxNum": 18,
                "StorageNodeMem": 8,
                "StorageNodeMinDisk": 20,
                "StorageNodeMinNum": 3,
                "StorageType": "CLOUD_HSSD"
            }
        ],
        "RequestId": "f2bed855-af44-46c8-bd47-e84fd52e5b16"
    }
}
```

**Example 2: 查询机型规格信息**



Input: 

```
tccli tdmysql DescribeSpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HybridNodeSpecs": [
            {
                "StorageNodeMaxDisk": 0,
                "StorageNodeMinNum": 0,
                "StorageNodeMinDisk": 0,
                "SpecCode": "1c2g",
                "StorageNodeCpu": 0,
                "StorageNodeMem": 0,
                "StorageNodeMaxNum": 0,
                "StorageType": "CLOUD_HSSD"
            }
        ],
        "RequestId": "f2bed855-af44-46c8-bd47-e84fd52e5b16"
    }
}
```

