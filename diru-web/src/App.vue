<template>
  <div id="app">
    <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" background-color="#545c64"
      text-color="#fff" active-text-color="#ffd04b">
      <el-menu-item index="1">数字图像小组</el-menu-item>
    </el-menu>

    <el-card style="margin-top: 20px;">
      <el-row>
        <el-col :span="11">
          <el-upload class="upload-demo" action="" :on-change="changeFile" :on-remove="handleRemove"  :show-file-list="false" :auto-upload="false">
            <el-button size="small" type="primary">预览图片</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件</div>
          </el-upload>
        </el-col>
        <el-col :span="2">
          <el-divider direction="vertical"></el-divider>
        </el-col>
        <el-col :span="2">
          <el-button type="primary" @click="handleUpload1">上传服务器</el-button>
        </el-col>
      </el-row>
    </el-card>
    <el-card style="margin-top: 20px;">
      <el-row>
        <el-col :span="11">
          <el-row style="margin-bottom: 10px;"><span class="demonstration">用户上传图片</span></el-row>
          <el-row>
            <el-image :src="image_src">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </el-row>
        </el-col>
        <el-col :span="2" class="image">
          <el-divider direction="vertical"></el-divider>
        </el-col>
        <el-col :span="11">
          <el-row style="margin-bottom: 10px;"><span class="demonstration">结果</span></el-row>
          <el-row>
            <el-image :src="res_src">
              <div slot="error" class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </el-row>
          <el-row>
            <el-radio-group v-if="category" v-model="filter" @change="handleFilter">
              <el-radio-button v-for="item in category"  :label="item"></el-radio-button>
              </el-radio-group>
          </el-row>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>
<script>
import imageApi from '@/api/image'
export default {
  data() {
    return {
      activeIndex2: '1',
      availble: false,
      fileList: [],
      src: '',
      image_src: '',
      res_src:'',
      category:[],
      filter:''

    }
  },
  methods: {
    changeFile(file, fileList) {
      this.src = file.raw;
      this.image_src = URL.createObjectURL(file.raw);
    },
    handleRemove(file, fileList){
      this.src = '';
      this.image_src = '',
      this.res_src = '',
      this.fileList = []
      this.category = []
    },
    //  根据下面的fuction改写成你们想要的
    handleUpload1(){
      // 这里写需要上传的api
      imageApi.fuc1(this.src).then(response=>{
        console.log(response)
        this.filter = []
        let data = response.data
        this.res_src =  'data:image/png;base64,' + data.file
        this.category = data.data
      })
      console.log(this.res_src)
    },
    handleFilter(){
        imageApi.fitler(this.src,this.filter).then(res=>{
          let data = res.data
          this.res_src =  'data:image/png;base64,' + data.file
        })
    }
  }
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.el-divider--vertical {
  height: 3em !important;
}

.image>.el-divider--vertical {
  height: 25em !important;
}


.el-image {
  width: 500px;
  height: 350px;
}

.image-slot{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background: #f5f7fa;
    color: #909399;
    font-size: 60px;
}
</style>
