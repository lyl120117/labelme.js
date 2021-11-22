import request from '@/utils/request'

export function uploadFiles(data, onUploadProgress) {
  console.log('##uploadFile')
  return request({
    url: '/upload',
    method: 'post',
    data,
    onUploadProgress
  })
}
