**Example 1: 查询dspm数据识别数据项详情**



Input: 

```
tccli csip DescribeDspmIdentifyRuleDetail --cli-unfold-argument  \
    --Id 10000 \
    --MemberId mem-12e1w112
```

Output: 
```
{
    "Response": {
        "Description": "1",
        "Id": 10000,
        "Name": "kyrie测试",
        "Status": 1,
        "StructuredRule": "{\n  \"NodeType\": \"operator\",\n  \"OptType\": \"or\",\n  \"RuleInfos\": [],\n  \"Nodes\": [\n    {\n      \"NodeType\": \"operator\",\n      \"OptType\": \"or\",\n      \"RuleInfos\": [\n        {\n          \"DataSourceType\": \"field_comment\",\n          \"RuleMethod\": \"match\",\n          \"RuleType\": \"regex\",\n          \"RuleContent\": \"(国家|国家代码)$\",\n          \"Parameters\": {\n            \"IsFullWordMatch\": \"false\",\n            \"IsIgnoreCase\": \"true\"\n          }\n        }\n      ],\n      \"Nodes\": []\n    },\n    {\n      \"NodeType\": \"operator\",\n      \"OptType\": \"and\",\n      \"RuleInfos\": [\n        {\n          \"DataSourceType\": \"field_name\",\n          \"RuleMethod\": \"match\",\n          \"RuleType\": \"keyword\",\n          \"RuleContent\": \"country\\n国家\",\n          \"Parameters\": {\n            \"IsFullWordMatch\": \"false\",\n            \"IsIgnoreCase\": \"true\"\n          }\n        },\n        {\n          \"DataSourceType\": \"field_name\",\n          \"RuleMethod\": \"match\",\n          \"RuleType\": \"keywordNotMatch\",\n          \"RuleContent\": \"side\\nmusic\\nroad\\nlife\\nstyle\\nfolk\\nhouse\\nyard\\nwide\",\n          \"Parameters\": {\n            \"IsFullWordMatch\": \"false\",\n            \"IsIgnoreCase\": \"true\"\n          }\n        }\n      ],\n      \"Nodes\": []\n    }\n  ]\n}",
        "Type": 1,
        "UnStructuredRule": "{\n  \"RegexRule\": {\n    \"Operator\": \"or\",\n    \"Contents\": [\n      {\n        \"RuleContent\": \"(?<=\\\\W)(中国|日本|韩国|朝鲜|蒙古|越南|柬埔寨|老挝|泰国|缅甸|菲律宾|文莱|马来西亚|新加坡|印度尼西亚|东帝汶|尼泊尔|不丹|巴基斯坦|印度|孟加拉国|马尔代夫|斯里兰卡|哈萨克斯坦|吉尔吉斯斯坦|塔吉克斯坦|乌兹别克斯坦|土库曼斯坦|阿富汗|伊朗|伊拉克|叙利亚|黎巴嫩|以色列|巴勒斯坦|约旦|沙特阿拉伯|巴林|卡塔尔|科威特|阿拉伯联合酋长国/阿联酋|阿曼|也门|格鲁吉亚|亚美尼亚|阿塞拜疆|土耳其|冰岛|丹麦|挪威|瑞典|芬兰|英国|爱尔兰|法国|摩纳哥|荷兰|比利时|卢森堡|德国|瑞士|列支敦士登|波兰|捷克|斯洛伐克|奥地利|匈牙利|爱沙尼亚|拉脱维亚|立陶宛|白俄罗斯|乌克兰|摩尔多瓦|俄罗斯|葡萄牙|西班牙|安道尔|意大利|圣马力诺|梵蒂冈|马耳他|斯洛文尼亚|克罗地亚|波黑|黑山|塞尔维亚|阿尔巴尼亚|北马其顿|保加利亚|希腊|罗马尼亚|塞浦路斯|埃及|利比亚|突尼斯|阿尔及利亚|摩洛哥|尼日尔|布基纳法索|马里|毛里塔尼亚|尼日利亚|贝宁|多哥|加纳|科特迪瓦|利比里亚|塞拉利昂|几内亚|几内亚比绍|塞内加尔|冈比亚|佛得角|乍得|中非|喀麦隆|刚果民主共和国|刚果共和国|加蓬|赤道几内亚|圣多美和普林西比|吉布提|索马里|厄立特里亚|埃塞俄比亚|苏丹|南苏丹|肯尼亚|坦桑尼亚|乌干达|卢旺达|布隆迪|塞舌尔|安哥拉|赞比亚|马拉维|莫桑比克|纳米比亚|博茨瓦纳|津巴布韦|南非|斯威士兰|莱索托|马达加斯加|毛里求斯|科摩罗|澳大利亚|新西兰|帕劳|密克罗尼西亚联邦|马绍尔群岛|瑙鲁|基里巴斯|巴布亚新几内亚|所罗门群岛|瓦努阿图|斐济|图瓦卢|萨摩亚|汤加|纽埃|库克群岛|加拿大|美国|墨西哥|危地马拉|伯利兹|萨尔瓦多|洪都拉斯|尼加拉瓜|哥斯达黎加|巴拿马|巴哈马|古巴|牙买加|海地|多米尼加|圣基茨和尼维斯|安提瓜和巴布达|多米尼克|圣卢西亚|巴巴多斯|圣文森特和格林纳丁斯|格林纳达|特立尼达和多巴哥|哥伦比亚|委内瑞拉|圭亚那|苏里南|厄瓜多尔|秘鲁|玻利维亚|巴西|智利|阿根廷|乌拉圭|巴拉圭|库拉索|China|Japan|South Korea|North Korea|Mongolia|Vietnam|Cambodia|Laos|Thailand|Myanmar|Philippines|Brunei|Malaysia|Singapore|Indonesia|Timor-Leste|Nepal|Bhutan|Pakistan|India|Bangladesh|Maldives|Sri Lanka|Kazakhstan|Kyrgyzstan|Tajikistan|Uzbekistan|Turkmenistan|Afghanistan|Iran|Iraq|Syria|Lebanon|Israel|Palestine|Jordan|Saudi Arabia|Bahrain|Qatar|Kuwait|United Arab Emirates|Oman|Yemen|Georgia|Armenia|Azerbaijan|Turkey|Iceland|Denmark|Norway|Sweden|Finland|The United Kingdom|Ireland|France|Monaco|Netherlands|Belgium|Luxembourg|Germany|Switzerland|Liechtenstein|Poland|Czechia|Slovakia|Austria|Hungary|Estonia|Latvia|Lithuania|Belarus|Ukraine|Moldova|Russian Federation|Portugal|Spain|Andorra|Italy|San Marino|Holy See|Malta|Slovenia|Croatia|Bosnia and Herzegovina|Montenegro|Serbia|Albania|North Macedonia|Bulgaria|Greece|Romania|Cyprus|Egypt|Libya|Tunisia|Algeria|Morocco|Niger|Burkina Faso|Mali|Mauritania|Nigeria|Benin|Togo|Ghana|Côte d'Ivoire|Liberia|Sierra Leone|Guinea|Guinea-Bissau|Senegal|Gambia|Cabo Verde|Chad|Central African Republic|Cameroon|The Democratic Republic of the Congo|Congo|Gabon|Equatorial Guinea|Sao Tome and Principe|Djibouti|Somalia|Eritrea|Ethiopia|Sudan|South Sudan|Kenya|Tanzania|Uganda|Rwanda|Burundi|Seychelles|Angola|Zambia|Malawi|Mozambique|Namibia|Botswana|Zimbabwe|South Africa|Eswatini|Lesotho|Madagascar|Mauritius|Comoros|Australia|New Zealand|Palau|Federated States of Micronesia|Marshall Islands|Nauru|Kiribati|Papua New Guinea|Solomon Islands|Vanuatu|Fiji|Tuvalu|Samoa|Tonga|Niue|Cook Islands|Canada|United States of America|Mexico|Guatemala|Belize|El Salvador|Honduras|Nicaragua|Costa Rica|Panama|Bahamas|Cuba|Jamaica|Haiti|Dominican Republic|Saint Kitts and Nevis|Antigua and Barbuda|Dominica|Saint Lucia|Barbados|Saint Vincent and the Grenadines|Grenada|Trinidad and Tobago|Colombia|Venezuela|Guyana|Suriname|Ecuador|Peru|Bolivia|Brazil|Chile|Argentina|Uruguay|Paraguay|Curaçao)(?=\\\\W)|(?i)(?<=((国家|国家代码|country|country_?code)\\\\W{1,7}))(\\\\d{2,3}|[A-Z]{2,3})(?=\\\\W)\",\n        \"IsIgnoreCase\": false\n      }\n    ]\n  },\n  \"AlgorithmRule\": {\n    \"Operator\": \"or\",\n    \"Contents\": []\n  },\n  \"KeywordRule\": {\n    \"Operator\": \"or\",\n    \"Contents\": [\n      {\n        \"RuleContent\": \"国家\",\n        \"IsIgnoreCase\": false\n      },\n      {\n        \"RuleContent\": \"country\",\n        \"IsIgnoreCase\": true\n      }\n    ]\n  },\n  \"IgnoreStringRule\": {\n    \"Operator\": \"or\",\n    \"Contents\": []\n  },\n  \"MaxMatchRule\": {\n    \"Length\": 20\n  },\n  \"GlobalKeywordRule\": {\n    \"Contents\": [],\n    \"IsIgnoreCase\": true\n  }\n}",
        "RequestId": "8667abd2-8e7e-4a9a-b30b-712a2e66d3b1"
    }
}
```

