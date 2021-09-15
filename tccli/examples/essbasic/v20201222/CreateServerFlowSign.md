**Example 1: 静默签署**



Input: 

```
tccli essbasic CreateServerFlowSign --cli-unfold-argument  \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --FlowId e9796ff652839ecb9c2402798f1dc7f9 \
    --SourceIp 172.16.0.1 \
    --SignComponents.0.ComponentId 4b07197c2a49d539c490b6fe43d4a3ae \
    --SignComponents.0.FileIndex 0 \
    --SignComponents.0.GenerateMode 0 \
    --SignComponents.0.ComponentValue 85a4d86c307f277ebf6e9ce2c8f7eb2c \
    --SignComponents.1.ComponentId 48b820f51115c76ce0ab19ef708d841c \
    --SignComponents.1.FileIndex 1 \
    --SignComponents.1.GenerateMode 0 \
    --SignComponents.2.ComponentPosX 122.12 \
    --SignComponents.2.ComponentType SIGN_SEAL \
    --SignComponents.2.ComponentPage 1 \
    --SignComponents.2.ComponentWidth 200 \
    --SignComponents.2.FileIndex 0 \
    --SignComponents.2.GenerateMode 0 \
    --SignComponents.2.ComponentHeight 300 \
    --SignComponents.2.ComponentValue 85a4d86c307f277ebf6e9ce2c8f7eb2c \
    --SignComponents.2.ComponentPosY 133.13
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609731093733170024",
        "SignStatus": 1
    }
}
```

