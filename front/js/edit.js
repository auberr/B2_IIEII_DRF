console.log('edit page')

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

var parameter = window.location.href
var plid = getParameterByName('pl_id')

window.onload = async function loadMylist() {
    const response = await fetch(`http://127.0.0.1:8000/musicplaylist/${plid}/detail/`, { method: "GET" })

    response_json = await response.json()
    console.log(response_json)

    const title = document.getElementById('page_title')
    if (response_json.playlist_title === null) {
        title.innerText = "playlist" + response_json.id + '수정'
    } else {
        title.innerText = response_json.playlist_title + '수정'
    }
    const my_list = document.getElementById('recommend_playlist')
    list_json = response_json.playlist_select_musics

    list_json.forEach(element => {
        const my_music = document.createElement("li")
        my_music.innerText = element.music_title + '\u00a0' + '-' + '\u00a0' + element.music_artist

        const img = document.createElement("IMG")
        img.setAttribute("src", element.music_img)

        my_list.appendChild(my_music)
        my_list.appendChild(img)
    });

    // 동적으로 input 값을 넣어서 생성하는 javascript code 
    const title_input = document.getElementById('titleinput')
    const my_title_input = document.createElement("input")
    my_title_input.setAttribute("value", response_json.playlist_title)
    my_title_input.setAttribute("class", "form-control")
    my_title_input.setAttribute("id", "title_input_update_box")
    title_input.appendChild(my_title_input)
    
    const content_input = document.getElementById('contentinput')
    const my_content_input = document.createElement("input")
    my_content_input.setAttribute("value", response_json.playlist_content)
    my_content_input.setAttribute("class", "form-control")
    my_content_input.setAttribute("id", "content_input_update_box")
    content_input.appendChild(my_content_input)




}

async function edit_playlist() {
    const token = localStorage.getItem('access')
    const title = document.getElementById("title_input_update_box").value
    const content = document.getElementById("content").value
    console.log(title, content)

    const response = await fetch(`http://127.0.0.1:8000/musicplaylist/${plid}/detail/`, {
        headers: {
            'Authorization': 'Bearer ' + token,
            'content-type': 'application/json',
        },
        method: 'PUT',
        body: JSON.stringify({
            "playlist_title": title,
            "playlist_content": content
        })
    }).then(window.location.replace("profile.html"))
    console.log(response)
    alert("완료");
}

async function delete_playlist() {
    const token = localStorage.getItem('access')
    let delete_msg = confirm("플레이리스트를 삭제할까요?");
    
    if (delete_msg){
    const response = await fetch(`http://127.0.0.1:8000/musicplaylist/${plid}/detail/`, {
        headers: {
            'Authorization': 'Bearer ' + token,
            'content-type': 'application/json',
        },
        method: 'DELETE',

    }).then(window.location.replace("profile.html"))
    console.log(response)
    alert("삭제 완료");
}}

function handleLogout(){
    localStorage.clear()
    window.location.replace("login.html")
}