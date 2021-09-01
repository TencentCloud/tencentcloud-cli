**Example 1: 获取某个事件的控制台输出**



Input: 

```
tccli tic DescribeStackEvent --cli-unfold-argument  \
    --EventId ent-spxin9pr
```

Output: 
```
{
    "Response": {
        "EventId": "ent-1armn3sg",
        "VersionId": "ver-87bun57q",
        "StackId": "stk-ld7ln3sh",
        "Type": "apply",
        "Status": "success",
        "EventMessage": "Message",
        "CreateTime": "2020-11-19T08:33:44.880Z",
        "ConsoleLog": "{\"eventId\":11963,\"message\":\"get the assignment plan task(event id:11963) and start\",\"pos\":1,\"tag\":\"system\",\"time\":1606374002497328796}\n{\"eventId\":11963,\"message\":\"the task passed the validity and completeness test\",\"pos\":2,\"tag\":\"system\",\"time\":1606374002533244238}\n{\"eventId\":11963,\"message\":\"prepare the files needed for the task\",\"pos\":3,\"tag\":\"system\",\"time\":1606374002533316203}\n{\"eventId\":11963,\"message\":\"\",\"pos\":4,\"tag\":\"finish\",\"time\":1606374005539862944}",
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

