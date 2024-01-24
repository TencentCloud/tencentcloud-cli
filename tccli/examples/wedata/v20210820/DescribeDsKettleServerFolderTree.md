**Example 1: 查询Kettle服务目录树**

FailedOperation

Input: 

```
tccli wedata DescribeDsKettleServerFolderTree --cli-unfold-argument  \
    --ProjectId abc \
    --Path abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "abc",
                "Title": "abc",
                "Name": "abc",
                "Type": "abc",
                "IsLeaf": true,
                "Path": "abc",
                "Children": [
                    {
                        "Id": "abc",
                        "Title": "abc",
                        "Name": "abc",
                        "Type": "abc",
                        "IsLeaf": true,
                        "Path": "abc",
                        "Children": [
                            {
                                "Id": "abc",
                                "Title": "abc",
                                "Name": "abc",
                                "Type": "abc",
                                "IsLeaf": true,
                                "Path": "abc",
                                "ExecuteCommand": "abc"
                            }
                        ],
                        "ExecuteCommand": "abc"
                    }
                ],
                "ExecuteCommand": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

