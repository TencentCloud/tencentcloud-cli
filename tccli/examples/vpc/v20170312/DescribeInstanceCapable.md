**Example 1: 查询机型能力**

查询机型能力

Input: 

```
tccli vpc DescribeInstanceCapable --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceCapableSet": [
            {
                "CapableType": "Trunking",
                "InstanceFamilySet": [
                    "S2",
                    "S1",
                    "CDH",
                    "S5"
                ]
            }
        ],
        "RequestId": "796bd5f4-92d5-4e49-8770-a46749cfb960"
    }
}
```

