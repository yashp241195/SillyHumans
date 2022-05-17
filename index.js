const express = require('express')
const morgan = require('morgan')
const bodyParser = require('body-parser')
// const cors = require('cors') 

const app = express()
// app.use(cors())
app.use(morgan('dev'));
app.use(bodyParser.json()); // for json data
// app.use(bodyParser.urlencoded({ extended: true })) // for form data
app.use(express.static("public"))


const PORT = process.env.PORT || 3005 

app.listen(PORT,()=>{
  console.log('Welcome to express rest api app')
})