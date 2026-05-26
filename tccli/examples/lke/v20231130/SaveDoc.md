**Example 1: SaveDoc**



Input: 

```
tccli lke SaveDoc --cli-unfold-argument  \
    --BotBizId 2055111415718175360 \
    --FileName 2024年-1-3-1.pdf \
    --FileType pdf \
    --CosUrl /corp/1747547736762744832/2055111415718175360/doc/OhcIrHUSClPEVusVlBjK-2057085760865765120.pdf \
    --ETag "4d81367c7a76d03cb3ef4d76630d0eae" \
    --CosHash 4395436907549135836 \
    --Size 499476 \
    --AttrRange 1 \
    --Source 0 \
    --WebUrl  \
    --ReferUrlType 0 \
    --ExpireStart 1779282442 \
    --IsRefer False \
    --Opt 2 \
    --CateBizId 0 \
    --IsDownload False \
    --SplitRule {"split_config_new":{"table_style":"md","rm_spec_symbol":1}} \
    --EnableScope 2
```

Output: 
```
{
    "Response": {
        "DocBizId": "2057086103297555520",
        "DuplicateFileCheckType": 0,
        "ErrorLink": "",
        "ErrorLinkText": "",
        "ErrorMsg": "",
        "RequestId": "343679e1-8ed7-4e4e-ac91-c6a1c14428b6"
    }
}
```

