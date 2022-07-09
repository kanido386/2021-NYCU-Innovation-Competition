# 2021 NYCU Global Digital Service & Innovation Competition

<img src="https://i.imgur.com/oPOYUFk.png" width="800">

## Topic
How to use Open Data combined with LINE Bot to improve medical and health care

## Presentation Video
https://www.youtube.com/watch?v=djUoMO8IMcU

## System Design
<img src="https://kanido386.github.io/2021/07/hackathon-line-hint/1.jpg" width="800">

- We used **Flask** and **FSM model** as the basic architecture of **LINE Bot**.
- Reading and writing databases with **Firebase Firestore**.
- Image upload and URL generation with **Firebase Storage**.
- Deployed LINE Bot server on **Heroku**.
- Deployed an ML model and a function with the **Algorithmia** platform to lighten the load on the server and reduce the space usage.
- Deployed **LIFF** pages with GitHub Pages.

## FSM State Diagram
<img src="https://kanido386.github.io/2021/07/hackathon-line-hint/2.jpg" width="800">

- Before coding, we used the FSM state diagram to design the architecture of the entire project functionality.
- With this state diagram, we can grasp the outline of the entire project, which makes coding easier!


For more details, see my blog post [黑客松 LINE Bot 賽前補帖](https://kanido386.github.io/2021/07/hackathon-line-hint/)!