**Example 1: 销毁EMR Serverless实例**



Input: 

```
tccli emr TerminateSLInstance --cli-unfold-argument  \
    --InstanceId emr-6vexh3oi
```

Output: 
```
{
    "Response": {
        "RequestId": "f4163a60-4801-449b-83d0-6f9ec2c7a07f"
    }
}
```

**Example 2: Lite HBase 销毁实例**

Lite HBase 销毁实例

Input: 

```
tccli emr TerminateSLInstance --cli-unfold-argument  \
    --InstanceId emr-8qrmc34c
```

Output: 
```
{
    "Response": {
        "RequestId": "a0b8ffca-02eb-47ea-9c93-a4c8db4e4585"
    }
}
```

