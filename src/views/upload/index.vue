<template>
  <div class="dashboard-container">
    <!-- <div class="dashboard-text">name: {{ name }}</div> -->
    <el-upload
      class="upload-demo"
      drag
      action=""
      multiple
      :http-request="uploadFile"
    >
      <i v-show="imgFlag == false" class="el-icon-upload" />
      <div v-show="imgFlag == false" class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <el-progress v-show="imgFlag == true" type="circle" :percentage="percent" style="margin-top: 25px" />
      <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
    </el-upload>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { uploadFiles } from '@/api/upload.js'

export default {
  name: 'Dashboard',
  data() {
    return {
      imgFlag: false,
      percent: 0
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    uploadFile(params) {
      var formData = new FormData()
      formData.append('file', params.file)
      console.log(params.file)
      uploadFiles(formData, progressEvent => {
        this.imgFlag = true
        const process = (progressEvent.loaded / progressEvent.total * 100 | 0)
        console.log('process: ' + process)
        this.percent = process
        if (process === 100) {
          this.imgFlag = false
          this.$message.success('上传成功！')
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
