# shiep-yjsgl
本系统封装了来自【上海电力大学研究生信息系统】的部分常用功能（见API列表），采用Flask框架构建后台应用 <br>

* 【目前提供的功能】：

|   功能名称              |              url              |
| ---------------------  | ----------------------------- |
|  成绩查询               |         /grade_query          |
|  获取所有需评教课程信息  |         /pj_lesson_query      |
|  获取课程评教表          |        /pj_table_query       |
|  提交评教               |        /post_pj              |
|  学生动态查询           |        /dt_query              |
|  动态城市查询           |        /dt_city_query         |
|  动态区域查询           |        /dt_area_query         |
|  动态申请提交           |        /dt_post               |  

* 【启动方式】: 进入根目录，在控制台输入命令 ```python app.py```


### 说明
为了更便于与上海电力大学研究生信息系统对照使用与阅读，本代码中大部分的【变量命名】采取【直接照搬上海电力大学研究生信息系统】的办法（所以如果命名太丑不是本作者的锅啦啦啦：）

-----------------------------------------------------------------------------

### API列表
#### 成绩查询
* url: /grade_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx}
  * username: 学号;
  * password: 密码;

#### 获取所有需评教课程信息
* url: /pj_lesson_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx}
  * username: 学号;
  * password: 密码;

#### 获取课程评教表
* url: /pj_table_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "bjid": xxxxx, "jsbh": xxxx}
  * username: 学号;
  * password: 密码;
  * bjid: 班级id;
  * jsbh: 教师编号;

#### 提交评教
* url: /post_pj
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "bjid": xxxxx, "jsbh": xxxx, "pj_json": xxxxxxx} <br>
  * username: 学号;
  * password: 密码;
  * bjid: 班级id;
  * jsbh: 教师编号;
  * pj_json: 学生提交的评教内容（json字符串）
  ```json
  // 示例 
  pj_json = [
    {
      "bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab",  // 班级id
      "jsbh": "2020010004",  // 教师编号
      "zbid": "1",   // 指标id
      "zt": "1",     // 状态
      "df": "8.0"    // 得分
     },
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "2", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "3", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "4", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "5", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "6", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "7", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "8", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "9", "zt": "1", "df": "8.0"},
    {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "10", "zt": "1", "df": "8.0"}
  ]
  ```
#### 学生动态查询
* url: /dt_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx}
  * username: 学号;
  * password: 密码;

#### 动态城市查询
* url: /dt_city_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "province_id": xx}
  * username: 学号;
  * password: 密码;
  * province_id: 省份id
  
#### 动态区域查询
* url: /dt_area_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "city_id": xx}
  * username: 学号;
  * password: 密码;
  * city_id: 城市id

#### 动态申请提交
* url: /dt_post
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "xc_json": xx}
  * username: 学号;
  * password: 密码;
  * xc_json: 行程详细内容（json字符串）
  ``` json
  // 示例
  xc_json = {
    "xcid": "7128",  // 行程id
    "bdsj": "2022-01-25 19:17:04",  // 变动时间
    "xclb": "03",  // 行程类别：1在校；2离沪在校；3离沪

    "provinceId": "33",
    "cityId": "3301",
    "areaId": "330101",
    "jdxx": "1",  // 街道详细
    
    // 此参数只用于离沪行程
    "jtfs": "03",  // 交通方式：1自驾；2大巴；3火车；4飞机

    // 以下两个参数只有在交通方式为火车/飞机才使用)
    "ccxx": "xxxxxx",  // 初次详细
    "hcxx": "xxxxxx",  // 换乘详细)
  }
  ```
