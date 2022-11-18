import service from '@/config/service'

const imageApi = {}

imageApi.fuc1 = (file)=>{
    const formData = new FormData();
    formData.append("file", file);
    return service({
        url: `${baseUrl}/uploadFile`,
        headers: {
            'Content-Type': 'multipart/form-data'
        },
        data: formData,
        method: 'post'

    })
}

export default payApi