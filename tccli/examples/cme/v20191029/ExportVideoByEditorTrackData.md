**Example 1: 使用视频编辑轨道数据导出视频**



Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform default_platform \
    --Definition 10 \
    --ExportDestination VOD \
    --TrackData [{\"id\":\"3e203081-0d40-4300-bbe5-0a6df9da9216\",\"type\":\"title\",\"order\":0,\"items\":[{\"id\":\"335c53f7-a4b5-4ffd-80f2-089d186e8bd8\",\"start_time\":4040,\"duration\":3000,\"type\":\"title\",\"content\":{\"template_id\":\"yj_templ_title_normal\",\"params\":{\"name\":\"yj_templ_title_black_transparent_bottom\",\"text\":\"hello\",\"text_x\":417,\"text_y\":141,\"text_width\":127,\"font\":\"SimHei\",\"font_color\":\"#ebebeb\",\"font_size\":60,\"bold\":0,\"italic\":0,\"layer_edit\":[{\"ind\":2,\"sw\":960,\"sc\":\"#000000\"}],\"shadow_color\":\"\",\"font_uline\":0,\"width\":960,\"height\":350,\"use_external_dimension\":1}},\"sizeRatio\":100,\"width\":960,\"height\":350,\"position\":{\"type\":\"ct\",\"x\":480,\"y\":270},\"asset_id\":\"281921553743709652@Public@CME\"}]},{\"id\":\"068383a0-5b03-4094-b5a0-8faacd69347b\",\"type\":\"video\",\"order\":1,\"items\":[{\"id\":\"d08c294a-28ee-4720-9915-1195ceb98eba\",\"start_time\":0,\"duration\":11600,\"type\":\"video\",\"section\":{\"from\":0,\"to\":11600},\"asset_id\":\"381921560306349928\",\"filter_asset_id\":\"\",\"operations\":[{\"type\":\"image_rotate\",\"params\":{\"angle\":0}}],\"position\":{\"x\":480,\"y\":270},\"width\":852,\"height\":480},{\"id\":\"69c746aa-863b-4ce7-807b-89fa7f1fc0e3\",\"start_time\":11600,\"duration\":4680,\"type\":\"video\",\"section\":{\"from\":0,\"to\":4680},\"asset_id\":\"381921560306349929\",\"filter_asset_id\":\"\",\"operations\":[{\"type\":\"image_rotate\",\"params\":{\"angle\":0}}],\"position\":{\"x\":480,\"y\":270},\"width\":852,\"height\":480},{\"id\":\"bfae2ebd-5332-428c-a8b6-edbc41b4c168\",\"start_time\":16280,\"duration\":10600,\"type\":\"video\",\"section\":{\"from\":1000,\"to\":11600},\"asset_id\":\"381921560306349928\",\"filter_asset_id\":\"\",\"width\":960,\"height\":541,\"position\":{\"x\":480,\"y\":270},\"operations\":[{\"type\":\"image_rotate\",\"params\":{\"angle\":0}}]}]}] \
    --VODExportInfo.Name 在线编辑视频 \
    --Operator 16556266637489
```

Output: 
```
{
    "Response": {
        "TaskId": "125009388839-tfusion-0a54392053f84053942f9308c49404d7",
        "RequestId": "0a543920-53f8-4053-942f-9308c49404d7"
    }
}
```

**Example 2: 指定轨道数据和宽高比导出视频**

当使用指定短边长度的视频编码配置以后，需要配合指定宽高比导出视频

Input: 

```
tccli cme ExportVideoByEditorTrackData --cli-unfold-argument  \
    --Platform test \
    --AspectRatio 16:9 \
    --TrackData [{"id":"84eaf25e-a515-4914-91d7-74accb6976b7","type":"video","order":0,"items":[{"id":"3285515a-3743-495d-87ba-f68f67a84f5f","start_time":0,"duration":16320,"type":"video","section":{"from":0,"to":16320},"asset_id":"6152cb87b5671f000135c7a1","filter_asset_id":"","width":960,"height":540,"position":{"x":540,"y":270},"operations":[{"type":"image_rotate","params":{"angle":0}},{"type":"audio_volumes","params":{"all":100}}],"is_new":true}]}] \
    --Definition 11 \
    --ExportDestination CME \
    --CMEExportInfo.Owner.Type PERSON \
    --CMEExportInfo.Owner.Id ed3fa411-73e6-4fd0-abe2-498bf5f9e7f0 \
    --CMEExportInfo.Name 新建项目 \
    --CMEExportInfo.ClassPath /成片
```

Output: 
```
{
    "Response": {
        "RequestId": "e86c730b-97c8-4e7d-b4a1-f5b28291e2b3",
        "TaskId": "1810000001-FusionCME-c85bf7f3b9b4c594fbd558800a6fecb5t"
    }
}
```

