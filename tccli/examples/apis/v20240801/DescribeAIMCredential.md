**Example 1: DescribeAIMCredential**

DescribeAIMCredential

Input: 

```
tccli apis DescribeAIMCredential --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID crd-8b468a40
```

Output: 
```
{
    "Response": {
        "Data": {
            "Access": [
                {
                    "Key": "testkey",
                    "Value": "testvalue"
                }
            ],
            "AppID": 1300273807,
            "CreateTime": "2026-03-16T03:58:35.358Z",
            "ID": "crd-8b468a40",
            "InstanceID": "ins-a7af1980",
            "LastUpdateTime": "2026-03-16T04:00:57.603Z",
            "Name": "newname",
            "Tags": [
                "testtag"
            ],
            "Type": "access",
            "Uin": "700001136234"
        },
        "RequestId": "4cb19b2a-81d3-4ccd-91a0-2d13d2690e7c"
    }
}
```

