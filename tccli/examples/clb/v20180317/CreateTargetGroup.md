**Example 1: Creating a target group**



Input: 

```
tccli clb CreateTargetGroup --cli-unfold-argument  \
    --TargetGroupName czhtest\
    --VpcId vpc-i1cnjuhx\
    --Port 80
```

Output: 
```
{
    "Response": {
        "TargetGroupId": "lbtg-815iz538",
        "RequestId": "9a4096dd-45a1-4e03-be8e-482a2fb48b59"
    }
}
```

