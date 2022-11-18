<template>
  <div id="app">
    <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" background-color="#545c64"
      text-color="#fff" active-text-color="#ffd04b">
      <el-menu-item index="1">数字图像小组</el-menu-item>
    </el-menu>

    <el-card style="margin-top: 20px;">
      <el-upload class="upload-demo" action="https://jsonplaceholder.typicode.com/posts/" :on-preview="handlePreview"
        :on-remove="handleRemove" :before-remove="beforeRemove" multiple :limit="1" :on-exceed="handleExceed"
        :file-list="fileList" show-file-list="false">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>
      <el-divider direction="vertical"></el-divider>
      <el-button type="primary">功能1</el-button>
      <el-button type="primary">功能2</el-button>
    </el-card>
    <el-card style="margin-top: 20px;">

    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activeIndex2: '1',
      availble: false,
      fileList:[]
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
</style>
