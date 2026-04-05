**Example 1: 修改监听器**



Input: 

```
tccli ga2 ModifyListener --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-5lkfom8v \
    --Name garendu-UDP-modify \
    --Description garendu-UDP-modify \
    --IdleTimeout 16
```

Output: 
```
{
    "Response": {
        "RequestId": "141079e2-c9ce-424f-9d5a-e0474b2da088",
        "TaskId": "24fdeb66-ad40-4a78-864c-15e49b6ef8d0"
    }
}
```

