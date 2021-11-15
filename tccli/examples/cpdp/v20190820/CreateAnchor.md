**Example 1: 微信视频号主播入驻**



Input: 

```
tccli cpdp CreateAnchor --cli-unfold-argument  \
    --AnchorUid wxc1300001 \
    --AnchorName 陈小丽 \
    --AnchorPhone htPFytIjJDPXW9sOmgtwTQ== \
    --AnchorAddress URvSZjJQPG0k+SRxVDLX2w== \
    --AnchorEmail WqN/MJI/n4AbNkUSfR5QbA== \
    --AnchorIdNo K1csRrg5tfardu/SfR5QbA== \
    --AnchorType WeChat \
    --AnchorExtendInfo.0.Type id_card_front \
    --AnchorExtendInfo.0.Value file.png \
    --AnchorExtendInfo.1.Type id_card_back \
    --AnchorExtendInfo.1.Value file.png \
    --AnchorExtendInfo.2.Type tax_type \
    --AnchorExtendInfo.2.Value 0 \
    --AnchorExtendInfo.3.Type channel_account \
    --AnchorExtendInfo.3.Value 3aWipNLSO4jtXus1P3mHMA==
```

Output: 
```
{
    "Response": {
        "AnchorId": "16267614198",
        "RequestId": "f64267a7-6a7d-4b0f-86de-b0e5fbae6847"
    }
}
```

