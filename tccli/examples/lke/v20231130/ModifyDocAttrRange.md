**Example 1: 批量修改文档的适用范围**



Input: 

```
tccli lke ModifyDocAttrRange --cli-unfold-argument  \
    --BotBizId 1742501052613230592 \
    --DocBizIds 1747174616331976704 \
    --AttrLabels.0.AttributeBizId 1759039436899221504 \
    --AttrLabels.0.Source 1 \
    --AttrLabels.0.LabelBizIds 0 \
    --AttrRange 2
```

Output: 
```
{
    "Response": {
        "RequestId": "e3338103-3165-49c0-b218-245be865cca5"
    }
}
```

