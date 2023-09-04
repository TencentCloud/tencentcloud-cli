**Example 1: 查询场景列表**

查询场景列表成功响应示例

Input: 

```
tccli weilingwith DescribeSceneList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "b7ab87c7-f4ae-420b-8e0a-ebfe0eb6e99f",
        "Result": {
            "SceneList": [
                {
                    "SceneId": "fa08fec8-8bf9-4902-8240-2c5c2777dfe4",
                    "SceneName": "测试数据发布",
                    "Version": "20230727161859024"
                },
                {
                    "SceneId": "d0d34f13-5aaa-4e3f-b9df-0c47a1f8b6e6",
                    "SceneName": "测试服务",
                    "Version": "20230630144242437"
                },
                {
                    "SceneId": "9fe1cb82-78fc-4758-ab03-a31dc0de8a89",
                    "SceneName": "幼儿园1F",
                    "Version": "20230705155913563"
                },
                {
                    "SceneId": "0fd68fbc-79b9-4909-8148-b43f431487f6",
                    "SceneName": "测试数据发布1",
                    "Version": "20230727163120647"
                },
                {
                    "SceneId": "2e730413-7d99-4c1a-8dac-b12d348e9bb6",
                    "SceneName": "小别墅单位修正",
                    "Version": "20230705155451510"
                },
                {
                    "SceneId": "12733040-c69a-4dd1-aa1e-2325bb331602",
                    "SceneName": "三层小别野",
                    "Version": "20230630151635871"
                },
                {
                    "SceneId": "0abe73dd-d06f-44f5-af82-43dea23af230",
                    "SceneName": "三层商务办公楼单位修正",
                    "Version": "20230705160410780"
                },
                {
                    "SceneId": "4738b98c-68d0-4f83-9487-9af9d020d310",
                    "SceneName": "测试数据发布2",
                    "Version": "20230727163522015"
                },
                {
                    "SceneId": "a9d100b1-1273-4d47-b573-6d286381809f",
                    "SceneName": "江森服务",
                    "Version": "20230630151236394"
                },
                {
                    "SceneId": "e9f2b87f-9078-4546-8d4f-99356ec3f82c",
                    "SceneName": "商务办公楼模型",
                    "Version": "20230630151240729"
                },
                {
                    "SceneId": "cc079cea-b5d0-4f9d-9b83-3f7b542e6614",
                    "SceneName": "BH-test",
                    "Version": "20230712150531776"
                },
                {
                    "SceneId": "bad4abea-5458-4580-a1ff-e0c979cc280d",
                    "SceneName": "54-building",
                    "Version": "20230727173527939"
                },
                {
                    "SceneId": "366bb60a-4fa7-4fa1-ad1b-1087f610860b",
                    "SceneName": "江森",
                    "Version": "20230630184023922"
                },
                {
                    "SceneId": "ac9ec5a4-3b0f-44f7-a71a-ddff713e0998",
                    "SceneName": "测试数据发布3",
                    "Version": "20230727163704761"
                },
                {
                    "SceneId": "8d0b8de6-78cc-450a-b027-b122a812e890",
                    "SceneName": "测试",
                    "Version": "20230727180522999"
                },
                {
                    "SceneId": "40379866-aff9-43d9-9e9d-c7c066ade9c7",
                    "SceneName": "测试数据发布4",
                    "Version": "20230727163735539"
                },
                {
                    "SceneId": "7ef255bd-0d0d-4bc0-b0d6-9737e063fcfa",
                    "SceneName": "54test",
                    "Version": "20230727181029004"
                },
                {
                    "SceneId": "5e1e1ad0-4085-4457-94ca-3e196065776e",
                    "SceneName": "我的测试aaa",
                    "Version": "20230731171838709"
                },
                {
                    "SceneId": "61a64cb0-2a63-4dc1-be27-f699b199e137",
                    "SceneName": "测试新增服务",
                    "Version": "20230801194415857"
                },
                {
                    "SceneId": "1698626f-a02e-4036-9584-40f93bd8c8fe",
                    "SceneName": "三层小别墅验证标高",
                    "Version": "20230711195949520"
                },
                {
                    "SceneId": "805395e7-31d6-4826-98b5-ec376027eee5",
                    "SceneName": "54new",
                    "Version": "20230731161731660"
                },
                {
                    "SceneId": "ec3fe40e-0673-403a-8b72-eb7245ff39f5",
                    "SceneName": "test322",
                    "Version": "20230731170522736"
                },
                {
                    "SceneId": "dfdbb59a-141c-40d8-a05c-636111f8145e",
                    "SceneName": "ga1122",
                    "Version": "20230816103702972"
                },
                {
                    "SceneId": "93effc84-8c4e-491a-8feb-1da4b278069d",
                    "SceneName": "测试我的服务啦啦啦",
                    "Version": "20230801195016874"
                },
                {
                    "SceneId": "3ea5e8ec-797b-4dd8-887c-9e85eb272b59",
                    "SceneName": "test1000",
                    "Version": "20230804153330669"
                },
                {
                    "SceneId": "e972baef-20c1-479d-aaef-c2b84b50e69c",
                    "SceneName": "发布参数测试",
                    "Version": "20230804172909247"
                },
                {
                    "SceneId": "3cc80e6c-0d69-419f-8e80-7e089f4ce286",
                    "SceneName": "路桥",
                    "Version": "20230808180259076"
                },
                {
                    "SceneId": "3e305d44-997f-4708-b1fa-264245b68ee4",
                    "SceneName": "test0002",
                    "Version": "20230804174001351"
                },
                {
                    "SceneId": "41a5d281-fc2a-46f6-83e4-c108159c8bf0",
                    "SceneName": "test003",
                    "Version": "20230804180150171"
                },
                {
                    "SceneId": "d1972cce-21b9-42de-a6ef-eebf6fc1a12c",
                    "SceneName": "测2",
                    "Version": "20230811145020507"
                },
                {
                    "SceneId": "a4f17670-3096-4632-a173-763d8eed4b24",
                    "SceneName": "test004",
                    "Version": "20230804182830425"
                },
                {
                    "SceneId": "0d24ea55-44e2-4fa1-ad28-92b064d7baac",
                    "SceneName": "testdgn",
                    "Version": "20230808180741817"
                },
                {
                    "SceneId": "7ff17051-713e-4c7e-9f61-053554ee8706",
                    "SceneName": "vfaaa",
                    "Version": "20230808105202390"
                },
                {
                    "SceneId": "23e8851c-3da6-40bb-a145-5fb228649a4d",
                    "SceneName": "testtest",
                    "Version": "20230807142948556"
                },
                {
                    "SceneId": "f17915fb-e95b-429f-9195-410f2a3a349e",
                    "SceneName": "原地质",
                    "Version": "20230808190956761"
                },
                {
                    "SceneId": "f3ceb0d9-9b9e-41fc-a829-48701718743b",
                    "SceneName": "修正dgn",
                    "Version": "20230808200842033"
                },
                {
                    "SceneId": "31694f6d-c29b-470a-9fe4-e4db3b882480",
                    "SceneName": "ceshi",
                    "Version": "20230809142831983"
                },
                {
                    "SceneId": "8500f89d-5cf6-4170-b6ef-6252b0b96fe5",
                    "SceneName": "Testtest",
                    "Version": "20230815104643390"
                },
                {
                    "SceneId": "bd9adb96-8f71-4f97-84fa-19eb49c88948",
                    "SceneName": "test00w",
                    "Version": "20230815163012361"
                }
            ]
        }
    }
}
```

**Example 2: 查询场景列表示例-prod**

查询场景列表示例-prod

Input: 

```
tccli weilingwith DescribeSceneList --cli-unfold-argument  \
    --WorkspaceId 1124 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "e8ac69f5-ee77-41c7-98f0-4c8719ce151e",
        "Result": {
            "SceneList": [
                {
                    "SceneId": "b26aeb0c-7715-478f-8270-115a88f4958d",
                    "SceneName": "回归2验证",
                    "Version": "20230615202042025"
                },
                {
                    "SceneId": "84d5fe8a-ea6b-4144-9af5-ad4534589e0b",
                    "SceneName": "回归01",
                    "Version": "20230615202654784"
                },
                {
                    "SceneId": "e41e558d-fc1a-40a8-ba60-867ff02e5092",
                    "SceneName": "回归011",
                    "Version": "20230615203039251"
                },
                {
                    "SceneId": "62add4e8-54a9-439e-8b6a-9c1f13d2f8c7",
                    "SceneName": "test(1)(1)(1)(1)(1)",
                    "Version": "20230616005825213"
                },
                {
                    "SceneId": "baf8418c-1b17-4c32-99e1-002f375a05d0",
                    "SceneName": "回归12",
                    "Version": "20230615203303801"
                },
                {
                    "SceneId": "4335d58f-602b-4f38-afb2-0e44573c0e27",
                    "SceneName": "回归01-底标高修改",
                    "Version": "20230615213006859"
                },
                {
                    "SceneId": "f3f655b5-27a0-401e-a8e1-cfbbf9738e92",
                    "SceneName": "test",
                    "Version": "20230616002041546"
                },
                {
                    "SceneId": "50accaba-dff7-4ee1-a676-4edc1ea59897",
                    "SceneName": "test(1)",
                    "Version": "20230616003658547"
                },
                {
                    "SceneId": "372ab2d4-b163-4377-9f15-faa63ded0e65",
                    "SceneName": "test(1)(1)(1)",
                    "Version": "20230616004614656"
                },
                {
                    "SceneId": "4fae00c4-def6-41ec-ab88-9497ed87779a",
                    "SceneName": "test(1)(1)(1)(1)",
                    "Version": "20230616004740399"
                },
                {
                    "SceneId": "6cb48ccb-ac15-4401-a41b-bf2f24ee4e48",
                    "SceneName": "阜外医院",
                    "Version": "20230616140720093"
                },
                {
                    "SceneId": "fe2fa6dd-4985-4394-914f-bafc6db4d038",
                    "SceneName": "好久好久",
                    "Version": "20230704102712493"
                },
                {
                    "SceneId": "ebd98dcb-e024-4b2a-9c8a-7edd255b45f9",
                    "SceneName": "测试法线",
                    "Version": "20230705220800744"
                },
                {
                    "SceneId": "6dd01099-472e-4741-b933-5a50331e9de4",
                    "SceneName": "换行1",
                    "Version": "20230704104225382"
                },
                {
                    "SceneId": "1a6f61e4-1616-49f1-bf30-19fdc14f358e",
                    "SceneName": "导入编辑测试",
                    "Version": "20230705221915959"
                },
                {
                    "SceneId": "571ac33b-1258-40c3-9bc7-55e508ee384f",
                    "SceneName": "验证修改",
                    "Version": "20230705225914902"
                },
                {
                    "SceneId": "54a5b4c9-bc12-489f-84f7-d7d787b250c3",
                    "SceneName": "验证配准",
                    "Version": "20230705230128637"
                },
                {
                    "SceneId": "31f257da-62a9-475f-ad55-dcd05334ef5d",
                    "SceneName": "test(1)",
                    "Version": "20230616004333025"
                },
                {
                    "SceneId": "b798bdb6-e70c-4f58-b6fd-ecc992845a16",
                    "SceneName": "验证建筑-bim模型楼层复制逻辑",
                    "Version": "20230707102558358"
                },
                {
                    "SceneId": "15fdc22c-3e69-4919-8c9f-a434332f7c7b",
                    "SceneName": "121",
                    "Version": "20230718145215925"
                },
                {
                    "SceneId": "e7ec508e-4516-4aab-9528-a5644f2490ec",
                    "SceneName": "滨海外壳集成编辑器数据",
                    "Version": "20230712193129991"
                },
                {
                    "SceneId": "0e357904-9b42-4f56-9e2b-462ff5f8e3a2",
                    "SceneName": "郑州CIM地质",
                    "Version": "20230713191738653"
                },
                {
                    "SceneId": "0d6819ce-12a8-4f43-85b4-ea7e2f500824",
                    "SceneName": "magTest",
                    "Version": "20230713194529513"
                },
                {
                    "SceneId": "5a968e10-d673-43ad-9813-b7aa2911bd63",
                    "SceneName": "郑州CIM-B",
                    "Version": "20230714093320141"
                },
                {
                    "SceneId": "cd2038b5-354d-4154-9e85-df523a3e1de9",
                    "SceneName": "郑州CIM-C",
                    "Version": "20230714101241138"
                },
                {
                    "SceneId": "dea2ac05-edea-4845-b280-42d0c2717142",
                    "SceneName": "滨海12",
                    "Version": "20230717210708851"
                },
                {
                    "SceneId": "dcb17b4e-0023-47f3-a495-b21e90d78c3d",
                    "SceneName": "三层小别墅rvt",
                    "Version": "20230717215119464"
                },
                {
                    "SceneId": "c51819fe-48e3-46e8-9b59-b9a7b5bd6f98",
                    "SceneName": "dizhi-test",
                    "Version": "20230724213033660"
                },
                {
                    "SceneId": "c79df355-697e-416f-9bf8-02fdd0daeb38",
                    "SceneName": "成大未调整位置",
                    "Version": "20230725200938887"
                },
                {
                    "SceneId": "5ef13ba7-51d2-48bc-996a-af39fccd34b7",
                    "SceneName": "地质-zz",
                    "Version": "20230726123425489"
                },
                {
                    "SceneId": "fc98f5c2-2e86-45a8-958e-5b5f8ed74098",
                    "SceneName": "rvt模型全量发布",
                    "Version": "20230731161418347"
                },
                {
                    "SceneId": "37275988-564f-4d6a-9a83-f8e66139d85a",
                    "SceneName": "地质DGN",
                    "Version": "20230815200226260"
                },
                {
                    "SceneId": "e136dc3d-e31f-4796-960c-3d72d20977f8",
                    "SceneName": "731revit",
                    "Version": "20230810141952165"
                },
                {
                    "SceneId": "7ae60a1a-baf8-4a0e-9a38-2ae7fce6b0fc",
                    "SceneName": "单个发布rvt",
                    "Version": "20230801214349885"
                },
                {
                    "SceneId": "0afd1428-a2cc-4b76-9ed8-0b0f86b48a8a",
                    "SceneName": "测试取样大大",
                    "Version": "20230815200657047"
                },
                {
                    "SceneId": "3642d2dd-2c76-4338-855f-1dbfed759fcc",
                    "SceneName": "郑州测试",
                    "Version": "20230817160720633"
                },
                {
                    "SceneId": "1570465b-9b7c-4861-8f16-5fd6ab7fcfb5",
                    "SceneName": "test",
                    "Version": "20230824192151326"
                },
                {
                    "SceneId": "922cd922-bf56-4131-aff0-84787aa41e80",
                    "SceneName": "成大3",
                    "Version": "20230725200606168"
                },
                {
                    "SceneId": "a04326ea-b7fc-4539-8de0-a2217a5f24f1",
                    "SceneName": "阜外医院(1)",
                    "Version": "20230828143707186"
                },
                {
                    "SceneId": "db6a1260-e3aa-4452-900a-d3051b2ddcf3",
                    "SceneName": "地质2-618",
                    "Version": "20230724221123184"
                },
                {
                    "SceneId": "d7c983d6-646d-4e33-8f05-b54eff28f00a",
                    "SceneName": "阜外",
                    "Version": "20230828150633511"
                },
                {
                    "SceneId": "96beff92-b88d-4cd1-a8f4-4bfcde1d4db7",
                    "SceneName": "测试建筑012",
                    "Version": "20230828161027282"
                },
                {
                    "SceneId": "76a3cea8-e4df-4403-8ec3-e680d610270e",
                    "SceneName": "测试建筑012-2",
                    "Version": "20230828161727992"
                },
                {
                    "SceneId": "4999cab6-2e60-4786-bc76-c81fd31c7eba",
                    "SceneName": "测试大模型发布",
                    "Version": "20230828211131266"
                },
                {
                    "SceneId": "a1b54411-38c2-43ea-88d4-7b38d293539b",
                    "SceneName": "未来城市鸟瞰-上传",
                    "Version": "20230828102844507"
                },
                {
                    "SceneId": "fa046369-b08a-4c4e-a7b2-45fecac1406b",
                    "SceneName": "工厂类模型",
                    "Version": "20230901100227099"
                }
            ]
        }
    }
}
```

