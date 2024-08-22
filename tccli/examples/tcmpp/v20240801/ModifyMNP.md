**Example 1: ModifyMNP**



Input: 

```
tccli tcmpp ModifyMNP --cli-unfold-argument  \
    --MNPType Logistics Services->1_Pickup/Delivery,Life Service->144_Lilliputian Services \
    --MNPName autotest_miniapp \
    --MNPIntro test \
    --MNPDesc test \
    --MNPId mpg9yjc0qbpkelik \
    --MNPIcon http://127.0.0.1/T04257DS9431720WTAG/console/20240820162809-c31a505943.png \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": 727
        },
        "RequestId": "36b3ccc2-a04a-4f73-82be-b472f5e4b262"
    }
}
```

