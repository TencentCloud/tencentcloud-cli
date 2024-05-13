**Example 1: 停止日志投递**



Input: 

```
tccli cynosdb StopCLSDelivery --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-o971o62r \
    --CLSTopicIds 83dc6703-f43a-4b95-92ec-267bdf9e48c3 2a289122-0b01-490b-be75-763da79621fe
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "347698da-03e4-4078-8d96-9a8b219c01a5"
    }
}
```

