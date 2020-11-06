**Example 1: Creating a spread placement group**

Create a spread placement group

Input: 

```
tccli cvm CreateDisasterRecoverGroup --cli-unfold-argument  \
    --Name 'Physical machine disaster recovery group' \
    --Type HOST
```

Output: 
```
{
    "Response": {
        "Type": "HOST",
        "DisasterRecoverGroupId": "ps-qajfd25h",
        "Name": "Physical machine disaster recovery group",
        "CvmQuotaTotal": 50,
        "CurrentNum": 0,
        "CreateTime": "2018-06-08T07:26:38Z",
        "RequestId": "21387009-9b9c-4b57-8fa2-8228f702ff6c"
    }
}
```

