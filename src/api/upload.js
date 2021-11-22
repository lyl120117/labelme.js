import request from '@/utils/request'

export function uploadFiles(data) {
  console.log('##uploadFile')
  return request({
    url: '/upload',
    method: 'post',
    data
  })
}
