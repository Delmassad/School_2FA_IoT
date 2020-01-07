import axios from 'axios';

const BACK_URL = 'http://127.0.0.1:5000/';
// const STATIC_URL = `${BACK_URL}static/`;

axios.get(`${BACK_URL}health`).then().catch(e => console.error('flask server not running : ' + e));

export async function getNames() {
    try {
        return (await axios.get(`${BACK_URL}names`)).data;
    } catch (error) {
        console.error(error);
    }
}

export async function savePicture(name) {
    axios.get(`${BACK_URL}save_picture/${name}`)
    .then(res => console.log(res.data))
    .catch(() => console.error(`cannot save face for ${name}`));
}

export async function getPicturesURL(name) {
        const filenames = (await axios.get(`${BACK_URL}get_pictures_urls/${name}`)).data;
        return filenames.map(f => `${BACK_URL}static/FaceRecognition/${name}/${f}`)
}

export async function whoAmI() {
    return (await axios.get(`${BACK_URL}who_am_i`)).data;
}
