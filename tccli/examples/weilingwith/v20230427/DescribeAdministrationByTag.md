**Example 1: 获取行政区划**

获取行政区划

Input: 

```
tccli weilingwith DescribeAdministrationByTag --cli-unfold-argument  \
    --ApplicationToken RQ7wnN7IMDutqe0JJ6t4MTqbBAePbryn \
    --WorkspaceId 1124 \
    --Tag 城市
```

Output: 
```
{
    "Response": {
        "RequestId": "c6802352-38e4-4a36-80dd-d80e57ce92a7",
        "Result": {
            "List": [
                {
                    "AdministrationCode": "130100",
                    "AdministrationName": "石家庄市"
                },
                {
                    "AdministrationCode": "130200",
                    "AdministrationName": "唐山市"
                },
                {
                    "AdministrationCode": "130300",
                    "AdministrationName": "秦皇岛市"
                },
                {
                    "AdministrationCode": "130400",
                    "AdministrationName": "邯郸市"
                },
                {
                    "AdministrationCode": "130500",
                    "AdministrationName": "邢台市"
                },
                {
                    "AdministrationCode": "130600",
                    "AdministrationName": "保定市"
                },
                {
                    "AdministrationCode": "130700",
                    "AdministrationName": "张家口市"
                },
                {
                    "AdministrationCode": "130800",
                    "AdministrationName": "承德市"
                },
                {
                    "AdministrationCode": "130900",
                    "AdministrationName": "沧州市"
                },
                {
                    "AdministrationCode": "131000",
                    "AdministrationName": "廊坊市"
                },
                {
                    "AdministrationCode": "131100",
                    "AdministrationName": "衡水市"
                },
                {
                    "AdministrationCode": "140100",
                    "AdministrationName": "太原市"
                },
                {
                    "AdministrationCode": "140200",
                    "AdministrationName": "大同市"
                },
                {
                    "AdministrationCode": "140300",
                    "AdministrationName": "阳泉市"
                },
                {
                    "AdministrationCode": "140400",
                    "AdministrationName": "长治市"
                },
                {
                    "AdministrationCode": "140500",
                    "AdministrationName": "晋城市"
                },
                {
                    "AdministrationCode": "140600",
                    "AdministrationName": "朔州市"
                },
                {
                    "AdministrationCode": "140700",
                    "AdministrationName": "晋中市"
                },
                {
                    "AdministrationCode": "140800",
                    "AdministrationName": "运城市"
                },
                {
                    "AdministrationCode": "140900",
                    "AdministrationName": "忻州市"
                },
                {
                    "AdministrationCode": "141000",
                    "AdministrationName": "临汾市"
                },
                {
                    "AdministrationCode": "141100",
                    "AdministrationName": "吕梁市"
                },
                {
                    "AdministrationCode": "150100",
                    "AdministrationName": "呼和浩特市"
                },
                {
                    "AdministrationCode": "150200",
                    "AdministrationName": "包头市"
                },
                {
                    "AdministrationCode": "150300",
                    "AdministrationName": "乌海市"
                },
                {
                    "AdministrationCode": "150400",
                    "AdministrationName": "赤峰市"
                },
                {
                    "AdministrationCode": "150500",
                    "AdministrationName": "通辽市"
                },
                {
                    "AdministrationCode": "150600",
                    "AdministrationName": "鄂尔多斯市"
                },
                {
                    "AdministrationCode": "150700",
                    "AdministrationName": "呼伦贝尔市"
                },
                {
                    "AdministrationCode": "150800",
                    "AdministrationName": "巴彦淖尔市"
                },
                {
                    "AdministrationCode": "150900",
                    "AdministrationName": "乌兰察布市"
                },
                {
                    "AdministrationCode": "152200",
                    "AdministrationName": "兴安盟"
                },
                {
                    "AdministrationCode": "152500",
                    "AdministrationName": "锡林郭勒盟"
                },
                {
                    "AdministrationCode": "152900",
                    "AdministrationName": "阿拉善盟"
                },
                {
                    "AdministrationCode": "210100",
                    "AdministrationName": "沈阳市"
                },
                {
                    "AdministrationCode": "210200",
                    "AdministrationName": "大连市"
                },
                {
                    "AdministrationCode": "210300",
                    "AdministrationName": "鞍山市"
                },
                {
                    "AdministrationCode": "210400",
                    "AdministrationName": "抚顺市"
                },
                {
                    "AdministrationCode": "210500",
                    "AdministrationName": "本溪市"
                },
                {
                    "AdministrationCode": "210600",
                    "AdministrationName": "丹东市"
                },
                {
                    "AdministrationCode": "210700",
                    "AdministrationName": "锦州市"
                },
                {
                    "AdministrationCode": "210800",
                    "AdministrationName": "营口市"
                },
                {
                    "AdministrationCode": "210900",
                    "AdministrationName": "阜新市"
                },
                {
                    "AdministrationCode": "211000",
                    "AdministrationName": "辽阳市"
                },
                {
                    "AdministrationCode": "211100",
                    "AdministrationName": "盘锦市"
                },
                {
                    "AdministrationCode": "211200",
                    "AdministrationName": "铁岭市"
                },
                {
                    "AdministrationCode": "211300",
                    "AdministrationName": "朝阳市"
                },
                {
                    "AdministrationCode": "211400",
                    "AdministrationName": "葫芦岛市"
                },
                {
                    "AdministrationCode": "220100",
                    "AdministrationName": "长春市"
                },
                {
                    "AdministrationCode": "220200",
                    "AdministrationName": "吉林市"
                },
                {
                    "AdministrationCode": "220300",
                    "AdministrationName": "四平市"
                },
                {
                    "AdministrationCode": "220400",
                    "AdministrationName": "辽源市"
                },
                {
                    "AdministrationCode": "220500",
                    "AdministrationName": "通化市"
                },
                {
                    "AdministrationCode": "220600",
                    "AdministrationName": "白山市"
                },
                {
                    "AdministrationCode": "220700",
                    "AdministrationName": "松原市"
                },
                {
                    "AdministrationCode": "220800",
                    "AdministrationName": "白城市"
                },
                {
                    "AdministrationCode": "222400",
                    "AdministrationName": "延边朝鲜族自治州"
                },
                {
                    "AdministrationCode": "230100",
                    "AdministrationName": "哈尔滨市"
                },
                {
                    "AdministrationCode": "230200",
                    "AdministrationName": "齐齐哈尔市"
                },
                {
                    "AdministrationCode": "230300",
                    "AdministrationName": "鸡西市"
                },
                {
                    "AdministrationCode": "230400",
                    "AdministrationName": "鹤岗市"
                },
                {
                    "AdministrationCode": "230500",
                    "AdministrationName": "双鸭山市"
                },
                {
                    "AdministrationCode": "230600",
                    "AdministrationName": "大庆市"
                },
                {
                    "AdministrationCode": "230700",
                    "AdministrationName": "伊春市"
                },
                {
                    "AdministrationCode": "230800",
                    "AdministrationName": "佳木斯市"
                },
                {
                    "AdministrationCode": "230900",
                    "AdministrationName": "七台河市"
                },
                {
                    "AdministrationCode": "231000",
                    "AdministrationName": "牡丹江市"
                },
                {
                    "AdministrationCode": "231100",
                    "AdministrationName": "黑河市"
                },
                {
                    "AdministrationCode": "231200",
                    "AdministrationName": "绥化市"
                },
                {
                    "AdministrationCode": "232700",
                    "AdministrationName": "大兴安岭地区"
                },
                {
                    "AdministrationCode": "320100",
                    "AdministrationName": "南京市"
                },
                {
                    "AdministrationCode": "320200",
                    "AdministrationName": "无锡市"
                },
                {
                    "AdministrationCode": "320300",
                    "AdministrationName": "徐州市"
                },
                {
                    "AdministrationCode": "320400",
                    "AdministrationName": "常州市"
                },
                {
                    "AdministrationCode": "320500",
                    "AdministrationName": "苏州市"
                },
                {
                    "AdministrationCode": "320600",
                    "AdministrationName": "南通市"
                },
                {
                    "AdministrationCode": "320700",
                    "AdministrationName": "连云港市"
                },
                {
                    "AdministrationCode": "320800",
                    "AdministrationName": "淮安市"
                },
                {
                    "AdministrationCode": "320900",
                    "AdministrationName": "盐城市"
                },
                {
                    "AdministrationCode": "321000",
                    "AdministrationName": "扬州市"
                },
                {
                    "AdministrationCode": "321100",
                    "AdministrationName": "镇江市"
                },
                {
                    "AdministrationCode": "321200",
                    "AdministrationName": "泰州市"
                },
                {
                    "AdministrationCode": "321300",
                    "AdministrationName": "宿迁市"
                },
                {
                    "AdministrationCode": "330100",
                    "AdministrationName": "杭州市"
                },
                {
                    "AdministrationCode": "330200",
                    "AdministrationName": "宁波市"
                },
                {
                    "AdministrationCode": "330300",
                    "AdministrationName": "温州市"
                },
                {
                    "AdministrationCode": "330400",
                    "AdministrationName": "嘉兴市"
                },
                {
                    "AdministrationCode": "330500",
                    "AdministrationName": "湖州市"
                },
                {
                    "AdministrationCode": "330600",
                    "AdministrationName": "绍兴市"
                },
                {
                    "AdministrationCode": "330700",
                    "AdministrationName": "金华市"
                },
                {
                    "AdministrationCode": "330800",
                    "AdministrationName": "衢州市"
                },
                {
                    "AdministrationCode": "330900",
                    "AdministrationName": "舟山市"
                },
                {
                    "AdministrationCode": "331000",
                    "AdministrationName": "台州市"
                },
                {
                    "AdministrationCode": "331100",
                    "AdministrationName": "丽水市"
                },
                {
                    "AdministrationCode": "340100",
                    "AdministrationName": "合肥市"
                },
                {
                    "AdministrationCode": "340200",
                    "AdministrationName": "芜湖市"
                },
                {
                    "AdministrationCode": "340300",
                    "AdministrationName": "蚌埠市"
                },
                {
                    "AdministrationCode": "340400",
                    "AdministrationName": "淮南市"
                },
                {
                    "AdministrationCode": "340500",
                    "AdministrationName": "马鞍山市"
                },
                {
                    "AdministrationCode": "340600",
                    "AdministrationName": "淮北市"
                },
                {
                    "AdministrationCode": "340700",
                    "AdministrationName": "铜陵市"
                },
                {
                    "AdministrationCode": "340800",
                    "AdministrationName": "安庆市"
                },
                {
                    "AdministrationCode": "341000",
                    "AdministrationName": "黄山市"
                },
                {
                    "AdministrationCode": "341100",
                    "AdministrationName": "滁州市"
                },
                {
                    "AdministrationCode": "341200",
                    "AdministrationName": "阜阳市"
                },
                {
                    "AdministrationCode": "341300",
                    "AdministrationName": "宿州市"
                },
                {
                    "AdministrationCode": "341500",
                    "AdministrationName": "六安市"
                },
                {
                    "AdministrationCode": "341600",
                    "AdministrationName": "亳州市"
                },
                {
                    "AdministrationCode": "341700",
                    "AdministrationName": "池州市"
                },
                {
                    "AdministrationCode": "341800",
                    "AdministrationName": "宣城市"
                },
                {
                    "AdministrationCode": "350100",
                    "AdministrationName": "福州市"
                },
                {
                    "AdministrationCode": "350200",
                    "AdministrationName": "厦门市"
                },
                {
                    "AdministrationCode": "350300",
                    "AdministrationName": "莆田市"
                },
                {
                    "AdministrationCode": "350400",
                    "AdministrationName": "三明市"
                },
                {
                    "AdministrationCode": "350500",
                    "AdministrationName": "泉州市"
                },
                {
                    "AdministrationCode": "350600",
                    "AdministrationName": "漳州市"
                },
                {
                    "AdministrationCode": "350700",
                    "AdministrationName": "南平市"
                },
                {
                    "AdministrationCode": "350800",
                    "AdministrationName": "龙岩市"
                },
                {
                    "AdministrationCode": "350900",
                    "AdministrationName": "宁德市"
                },
                {
                    "AdministrationCode": "360100",
                    "AdministrationName": "南昌市"
                },
                {
                    "AdministrationCode": "360200",
                    "AdministrationName": "景德镇市"
                },
                {
                    "AdministrationCode": "360300",
                    "AdministrationName": "萍乡市"
                },
                {
                    "AdministrationCode": "360400",
                    "AdministrationName": "九江市"
                },
                {
                    "AdministrationCode": "360500",
                    "AdministrationName": "新余市"
                },
                {
                    "AdministrationCode": "360600",
                    "AdministrationName": "鹰潭市"
                },
                {
                    "AdministrationCode": "360700",
                    "AdministrationName": "赣州市"
                },
                {
                    "AdministrationCode": "360800",
                    "AdministrationName": "吉安市"
                },
                {
                    "AdministrationCode": "360900",
                    "AdministrationName": "宜春市"
                },
                {
                    "AdministrationCode": "361000",
                    "AdministrationName": "抚州市"
                },
                {
                    "AdministrationCode": "361100",
                    "AdministrationName": "上饶市"
                },
                {
                    "AdministrationCode": "370100",
                    "AdministrationName": "济南市"
                },
                {
                    "AdministrationCode": "370200",
                    "AdministrationName": "青岛市"
                },
                {
                    "AdministrationCode": "370300",
                    "AdministrationName": "淄博市"
                },
                {
                    "AdministrationCode": "370400",
                    "AdministrationName": "枣庄市"
                },
                {
                    "AdministrationCode": "370500",
                    "AdministrationName": "东营市"
                },
                {
                    "AdministrationCode": "370600",
                    "AdministrationName": "烟台市"
                },
                {
                    "AdministrationCode": "370700",
                    "AdministrationName": "潍坊市"
                },
                {
                    "AdministrationCode": "370800",
                    "AdministrationName": "济宁市"
                },
                {
                    "AdministrationCode": "370900",
                    "AdministrationName": "泰安市"
                },
                {
                    "AdministrationCode": "371000",
                    "AdministrationName": "威海市"
                },
                {
                    "AdministrationCode": "371100",
                    "AdministrationName": "日照市"
                },
                {
                    "AdministrationCode": "371300",
                    "AdministrationName": "临沂市"
                },
                {
                    "AdministrationCode": "371400",
                    "AdministrationName": "德州市"
                },
                {
                    "AdministrationCode": "371500",
                    "AdministrationName": "聊城市"
                },
                {
                    "AdministrationCode": "371600",
                    "AdministrationName": "滨州市"
                },
                {
                    "AdministrationCode": "371700",
                    "AdministrationName": "菏泽市"
                },
                {
                    "AdministrationCode": "410100",
                    "AdministrationName": "郑州市"
                },
                {
                    "AdministrationCode": "410200",
                    "AdministrationName": "开封市"
                },
                {
                    "AdministrationCode": "410300",
                    "AdministrationName": "洛阳市"
                },
                {
                    "AdministrationCode": "410400",
                    "AdministrationName": "平顶山市"
                },
                {
                    "AdministrationCode": "410500",
                    "AdministrationName": "安阳市"
                },
                {
                    "AdministrationCode": "410600",
                    "AdministrationName": "鹤壁市"
                },
                {
                    "AdministrationCode": "410700",
                    "AdministrationName": "新乡市"
                },
                {
                    "AdministrationCode": "410800",
                    "AdministrationName": "焦作市"
                },
                {
                    "AdministrationCode": "410900",
                    "AdministrationName": "濮阳市"
                },
                {
                    "AdministrationCode": "411000",
                    "AdministrationName": "许昌市"
                },
                {
                    "AdministrationCode": "411100",
                    "AdministrationName": "漯河市"
                },
                {
                    "AdministrationCode": "411200",
                    "AdministrationName": "三门峡市"
                },
                {
                    "AdministrationCode": "411300",
                    "AdministrationName": "南阳市"
                },
                {
                    "AdministrationCode": "411400",
                    "AdministrationName": "商丘市"
                },
                {
                    "AdministrationCode": "411500",
                    "AdministrationName": "信阳市"
                },
                {
                    "AdministrationCode": "411600",
                    "AdministrationName": "周口市"
                },
                {
                    "AdministrationCode": "411700",
                    "AdministrationName": "驻马店市"
                },
                {
                    "AdministrationCode": "420100",
                    "AdministrationName": "武汉市"
                },
                {
                    "AdministrationCode": "420200",
                    "AdministrationName": "黄石市"
                },
                {
                    "AdministrationCode": "420300",
                    "AdministrationName": "十堰市"
                },
                {
                    "AdministrationCode": "420500",
                    "AdministrationName": "宜昌市"
                },
                {
                    "AdministrationCode": "420600",
                    "AdministrationName": "襄阳市"
                },
                {
                    "AdministrationCode": "420700",
                    "AdministrationName": "鄂州市"
                },
                {
                    "AdministrationCode": "420800",
                    "AdministrationName": "荆门市"
                },
                {
                    "AdministrationCode": "420900",
                    "AdministrationName": "孝感市"
                },
                {
                    "AdministrationCode": "421000",
                    "AdministrationName": "荆州市"
                },
                {
                    "AdministrationCode": "421100",
                    "AdministrationName": "黄冈市"
                },
                {
                    "AdministrationCode": "421200",
                    "AdministrationName": "咸宁市"
                },
                {
                    "AdministrationCode": "421300",
                    "AdministrationName": "随州市"
                },
                {
                    "AdministrationCode": "422800",
                    "AdministrationName": "恩施土家族苗族自治州"
                },
                {
                    "AdministrationCode": "430100",
                    "AdministrationName": "长沙市"
                },
                {
                    "AdministrationCode": "430200",
                    "AdministrationName": "株洲市"
                },
                {
                    "AdministrationCode": "430300",
                    "AdministrationName": "湘潭市"
                },
                {
                    "AdministrationCode": "430400",
                    "AdministrationName": "衡阳市"
                },
                {
                    "AdministrationCode": "430500",
                    "AdministrationName": "邵阳市"
                },
                {
                    "AdministrationCode": "430600",
                    "AdministrationName": "岳阳市"
                },
                {
                    "AdministrationCode": "430700",
                    "AdministrationName": "常德市"
                },
                {
                    "AdministrationCode": "430800",
                    "AdministrationName": "张家界市"
                },
                {
                    "AdministrationCode": "430900",
                    "AdministrationName": "益阳市"
                },
                {
                    "AdministrationCode": "431000",
                    "AdministrationName": "郴州市"
                },
                {
                    "AdministrationCode": "431100",
                    "AdministrationName": "永州市"
                },
                {
                    "AdministrationCode": "431200",
                    "AdministrationName": "怀化市"
                },
                {
                    "AdministrationCode": "431300",
                    "AdministrationName": "娄底市"
                },
                {
                    "AdministrationCode": "433100",
                    "AdministrationName": "湘西土家族苗族自治州"
                },
                {
                    "AdministrationCode": "440100",
                    "AdministrationName": "广州市"
                },
                {
                    "AdministrationCode": "440200",
                    "AdministrationName": "韶关市"
                },
                {
                    "AdministrationCode": "440300",
                    "AdministrationName": "深圳市"
                },
                {
                    "AdministrationCode": "440400",
                    "AdministrationName": "珠海市"
                },
                {
                    "AdministrationCode": "440500",
                    "AdministrationName": "汕头市"
                },
                {
                    "AdministrationCode": "440600",
                    "AdministrationName": "佛山市"
                },
                {
                    "AdministrationCode": "440700",
                    "AdministrationName": "江门市"
                },
                {
                    "AdministrationCode": "440800",
                    "AdministrationName": "湛江市"
                },
                {
                    "AdministrationCode": "440900",
                    "AdministrationName": "茂名市"
                },
                {
                    "AdministrationCode": "441200",
                    "AdministrationName": "肇庆市"
                },
                {
                    "AdministrationCode": "441300",
                    "AdministrationName": "惠州市"
                },
                {
                    "AdministrationCode": "441400",
                    "AdministrationName": "梅州市"
                },
                {
                    "AdministrationCode": "441500",
                    "AdministrationName": "汕尾市"
                },
                {
                    "AdministrationCode": "441600",
                    "AdministrationName": "河源市"
                },
                {
                    "AdministrationCode": "441700",
                    "AdministrationName": "阳江市"
                },
                {
                    "AdministrationCode": "441800",
                    "AdministrationName": "清远市"
                },
                {
                    "AdministrationCode": "441900",
                    "AdministrationName": "东莞市"
                },
                {
                    "AdministrationCode": "442000",
                    "AdministrationName": "中山市"
                },
                {
                    "AdministrationCode": "445100",
                    "AdministrationName": "潮州市"
                },
                {
                    "AdministrationCode": "445200",
                    "AdministrationName": "揭阳市"
                },
                {
                    "AdministrationCode": "445300",
                    "AdministrationName": "云浮市"
                },
                {
                    "AdministrationCode": "450100",
                    "AdministrationName": "南宁市"
                },
                {
                    "AdministrationCode": "450200",
                    "AdministrationName": "柳州市"
                },
                {
                    "AdministrationCode": "450300",
                    "AdministrationName": "桂林市"
                },
                {
                    "AdministrationCode": "450400",
                    "AdministrationName": "梧州市"
                },
                {
                    "AdministrationCode": "450500",
                    "AdministrationName": "北海市"
                },
                {
                    "AdministrationCode": "450600",
                    "AdministrationName": "防城港市"
                },
                {
                    "AdministrationCode": "450700",
                    "AdministrationName": "钦州市"
                },
                {
                    "AdministrationCode": "450800",
                    "AdministrationName": "贵港市"
                },
                {
                    "AdministrationCode": "450900",
                    "AdministrationName": "玉林市"
                },
                {
                    "AdministrationCode": "451000",
                    "AdministrationName": "百色市"
                },
                {
                    "AdministrationCode": "451100",
                    "AdministrationName": "贺州市"
                },
                {
                    "AdministrationCode": "451200",
                    "AdministrationName": "河池市"
                },
                {
                    "AdministrationCode": "451300",
                    "AdministrationName": "来宾市"
                },
                {
                    "AdministrationCode": "451400",
                    "AdministrationName": "崇左市"
                },
                {
                    "AdministrationCode": "460100",
                    "AdministrationName": "海口市"
                },
                {
                    "AdministrationCode": "460200",
                    "AdministrationName": "三亚市"
                },
                {
                    "AdministrationCode": "460300",
                    "AdministrationName": "三沙市"
                },
                {
                    "AdministrationCode": "460400",
                    "AdministrationName": "儋州市"
                },
                {
                    "AdministrationCode": "510100",
                    "AdministrationName": "成都市"
                },
                {
                    "AdministrationCode": "510300",
                    "AdministrationName": "自贡市"
                },
                {
                    "AdministrationCode": "510400",
                    "AdministrationName": "攀枝花市"
                },
                {
                    "AdministrationCode": "510500",
                    "AdministrationName": "泸州市"
                },
                {
                    "AdministrationCode": "510600",
                    "AdministrationName": "德阳市"
                },
                {
                    "AdministrationCode": "510700",
                    "AdministrationName": "绵阳市"
                },
                {
                    "AdministrationCode": "510800",
                    "AdministrationName": "广元市"
                },
                {
                    "AdministrationCode": "510900",
                    "AdministrationName": "遂宁市"
                },
                {
                    "AdministrationCode": "511000",
                    "AdministrationName": "内江市"
                },
                {
                    "AdministrationCode": "511100",
                    "AdministrationName": "乐山市"
                },
                {
                    "AdministrationCode": "511300",
                    "AdministrationName": "南充市"
                },
                {
                    "AdministrationCode": "511400",
                    "AdministrationName": "眉山市"
                },
                {
                    "AdministrationCode": "511500",
                    "AdministrationName": "宜宾市"
                },
                {
                    "AdministrationCode": "511600",
                    "AdministrationName": "广安市"
                },
                {
                    "AdministrationCode": "511700",
                    "AdministrationName": "达州市"
                },
                {
                    "AdministrationCode": "511800",
                    "AdministrationName": "雅安市"
                },
                {
                    "AdministrationCode": "511900",
                    "AdministrationName": "巴中市"
                },
                {
                    "AdministrationCode": "512000",
                    "AdministrationName": "资阳市"
                },
                {
                    "AdministrationCode": "513200",
                    "AdministrationName": "阿坝藏族羌族自治州"
                },
                {
                    "AdministrationCode": "513300",
                    "AdministrationName": "甘孜藏族自治州"
                },
                {
                    "AdministrationCode": "513400",
                    "AdministrationName": "凉山彝族自治州"
                },
                {
                    "AdministrationCode": "520100",
                    "AdministrationName": "贵阳市"
                },
                {
                    "AdministrationCode": "520200",
                    "AdministrationName": "六盘水市"
                },
                {
                    "AdministrationCode": "520300",
                    "AdministrationName": "遵义市"
                },
                {
                    "AdministrationCode": "520400",
                    "AdministrationName": "安顺市"
                },
                {
                    "AdministrationCode": "520500",
                    "AdministrationName": "毕节市"
                },
                {
                    "AdministrationCode": "520600",
                    "AdministrationName": "铜仁市"
                },
                {
                    "AdministrationCode": "522300",
                    "AdministrationName": "黔西南布依族苗族自治州"
                },
                {
                    "AdministrationCode": "522600",
                    "AdministrationName": "黔东南苗族侗族自治州"
                },
                {
                    "AdministrationCode": "522700",
                    "AdministrationName": "黔南布依族苗族自治州"
                },
                {
                    "AdministrationCode": "530100",
                    "AdministrationName": "昆明市"
                },
                {
                    "AdministrationCode": "530300",
                    "AdministrationName": "曲靖市"
                },
                {
                    "AdministrationCode": "530400",
                    "AdministrationName": "玉溪市"
                },
                {
                    "AdministrationCode": "530500",
                    "AdministrationName": "保山市"
                },
                {
                    "AdministrationCode": "530600",
                    "AdministrationName": "昭通市"
                },
                {
                    "AdministrationCode": "530700",
                    "AdministrationName": "丽江市"
                },
                {
                    "AdministrationCode": "530800",
                    "AdministrationName": "普洱市"
                },
                {
                    "AdministrationCode": "530900",
                    "AdministrationName": "临沧市"
                },
                {
                    "AdministrationCode": "532300",
                    "AdministrationName": "楚雄彝族自治州"
                },
                {
                    "AdministrationCode": "532500",
                    "AdministrationName": "红河哈尼族彝族自治州"
                },
                {
                    "AdministrationCode": "532600",
                    "AdministrationName": "文山壮族苗族自治州"
                },
                {
                    "AdministrationCode": "532800",
                    "AdministrationName": "西双版纳傣族自治州"
                },
                {
                    "AdministrationCode": "532900",
                    "AdministrationName": "大理白族自治州"
                },
                {
                    "AdministrationCode": "533100",
                    "AdministrationName": "德宏傣族景颇族自治州"
                },
                {
                    "AdministrationCode": "533300",
                    "AdministrationName": "怒江傈僳族自治州"
                },
                {
                    "AdministrationCode": "533400",
                    "AdministrationName": "迪庆藏族自治州"
                },
                {
                    "AdministrationCode": "540100",
                    "AdministrationName": "拉萨市"
                },
                {
                    "AdministrationCode": "540200",
                    "AdministrationName": "日喀则市"
                },
                {
                    "AdministrationCode": "540300",
                    "AdministrationName": "昌都市"
                },
                {
                    "AdministrationCode": "540400",
                    "AdministrationName": "林芝市"
                },
                {
                    "AdministrationCode": "540500",
                    "AdministrationName": "山南市"
                },
                {
                    "AdministrationCode": "540600",
                    "AdministrationName": "那曲市"
                },
                {
                    "AdministrationCode": "542500",
                    "AdministrationName": "阿里地区"
                },
                {
                    "AdministrationCode": "610100",
                    "AdministrationName": "西安市"
                },
                {
                    "AdministrationCode": "610200",
                    "AdministrationName": "铜川市"
                },
                {
                    "AdministrationCode": "610300",
                    "AdministrationName": "宝鸡市"
                },
                {
                    "AdministrationCode": "610400",
                    "AdministrationName": "咸阳市"
                },
                {
                    "AdministrationCode": "610500",
                    "AdministrationName": "渭南市"
                },
                {
                    "AdministrationCode": "610600",
                    "AdministrationName": "延安市"
                },
                {
                    "AdministrationCode": "610700",
                    "AdministrationName": "汉中市"
                },
                {
                    "AdministrationCode": "610800",
                    "AdministrationName": "榆林市"
                },
                {
                    "AdministrationCode": "610900",
                    "AdministrationName": "安康市"
                },
                {
                    "AdministrationCode": "611000",
                    "AdministrationName": "商洛市"
                },
                {
                    "AdministrationCode": "620100",
                    "AdministrationName": "兰州市"
                },
                {
                    "AdministrationCode": "620200",
                    "AdministrationName": "嘉峪关市"
                },
                {
                    "AdministrationCode": "620300",
                    "AdministrationName": "金昌市"
                },
                {
                    "AdministrationCode": "620400",
                    "AdministrationName": "白银市"
                },
                {
                    "AdministrationCode": "620500",
                    "AdministrationName": "天水市"
                },
                {
                    "AdministrationCode": "620600",
                    "AdministrationName": "武威市"
                },
                {
                    "AdministrationCode": "620700",
                    "AdministrationName": "张掖市"
                },
                {
                    "AdministrationCode": "620800",
                    "AdministrationName": "平凉市"
                },
                {
                    "AdministrationCode": "620900",
                    "AdministrationName": "酒泉市"
                },
                {
                    "AdministrationCode": "621000",
                    "AdministrationName": "庆阳市"
                },
                {
                    "AdministrationCode": "621100",
                    "AdministrationName": "定西市"
                },
                {
                    "AdministrationCode": "621200",
                    "AdministrationName": "陇南市"
                },
                {
                    "AdministrationCode": "622900",
                    "AdministrationName": "临夏回族自治州"
                },
                {
                    "AdministrationCode": "623000",
                    "AdministrationName": "甘南藏族自治州"
                },
                {
                    "AdministrationCode": "630100",
                    "AdministrationName": "西宁市"
                },
                {
                    "AdministrationCode": "630200",
                    "AdministrationName": "海东市"
                },
                {
                    "AdministrationCode": "632200",
                    "AdministrationName": "海北藏族自治州"
                },
                {
                    "AdministrationCode": "632300",
                    "AdministrationName": "黄南藏族自治州"
                },
                {
                    "AdministrationCode": "632500",
                    "AdministrationName": "海南藏族自治州"
                },
                {
                    "AdministrationCode": "632600",
                    "AdministrationName": "果洛藏族自治州"
                },
                {
                    "AdministrationCode": "632700",
                    "AdministrationName": "玉树藏族自治州"
                },
                {
                    "AdministrationCode": "632800",
                    "AdministrationName": "海西蒙古族藏族自治州"
                },
                {
                    "AdministrationCode": "640100",
                    "AdministrationName": "银川市"
                },
                {
                    "AdministrationCode": "640200",
                    "AdministrationName": "石嘴山市"
                },
                {
                    "AdministrationCode": "640300",
                    "AdministrationName": "吴忠市"
                },
                {
                    "AdministrationCode": "640400",
                    "AdministrationName": "固原市"
                },
                {
                    "AdministrationCode": "640500",
                    "AdministrationName": "中卫市"
                },
                {
                    "AdministrationCode": "650100",
                    "AdministrationName": "乌鲁木齐市"
                },
                {
                    "AdministrationCode": "650200",
                    "AdministrationName": "克拉玛依市"
                },
                {
                    "AdministrationCode": "650400",
                    "AdministrationName": "吐鲁番市"
                },
                {
                    "AdministrationCode": "650500",
                    "AdministrationName": "哈密市"
                },
                {
                    "AdministrationCode": "652300",
                    "AdministrationName": "昌吉回族自治州"
                },
                {
                    "AdministrationCode": "652700",
                    "AdministrationName": "博尔塔拉蒙古自治州"
                },
                {
                    "AdministrationCode": "652800",
                    "AdministrationName": "巴音郭楞蒙古自治州"
                },
                {
                    "AdministrationCode": "652900",
                    "AdministrationName": "阿克苏地区"
                },
                {
                    "AdministrationCode": "653000",
                    "AdministrationName": "克孜勒苏柯尔克孜自治州"
                },
                {
                    "AdministrationCode": "653100",
                    "AdministrationName": "喀什地区"
                },
                {
                    "AdministrationCode": "653200",
                    "AdministrationName": "和田地区"
                },
                {
                    "AdministrationCode": "654000",
                    "AdministrationName": "伊犁哈萨克自治州"
                },
                {
                    "AdministrationCode": "654200",
                    "AdministrationName": "塔城地区"
                },
                {
                    "AdministrationCode": "654300",
                    "AdministrationName": "阿勒泰地区"
                }
            ]
        }
    }
}
```

