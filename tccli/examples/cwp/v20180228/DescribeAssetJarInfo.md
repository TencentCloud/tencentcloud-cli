**Example 1: 获取Jar包详情**



Input: 

```
tccli cwp DescribeAssetJarInfo --cli-unfold-argument  \
    --Quuid acdd5474-6360-4fd4-bfc7-843162cb8116 \
    --Uuid acdd5474-6360-4fd4-bfc7-843162cb8116 \
    --Id 1024
```

Output: 
```
{
    "Response": {
        "Jar": {
            "Status": 1,
            "OsInfo": "CentOs Bit64",
            "UpdateTime": "2024-10-11 12:23:34",
            "Name": "test-name",
            "Process": [
                {
                    "Status": "S",
                    "Name": "test-name",
                    "Version": "0.1.1",
                    "User": "root",
                    "StartTime": "2024-10-11 12:23:34",
                    "Path": "/root"
                }
            ],
            "MachineName": "test-name",
            "Version": "0.1.1",
            "Path": "/root",
            "Type": 1,
            "MachineIp": "10.0.0.11",
            "Md5": "708cae4cf814c3deda4208da228fad4e"
        },
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

