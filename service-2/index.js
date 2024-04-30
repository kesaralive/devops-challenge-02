import express from "express";
import cors from "cors";
// import router from "./routes/helloRoutes";

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const router = express.Router();
app.use(router);

router.get("/", (req, res) => {
  res.send({ message: "Hello from express-js-service!" });
});

app.use(
  cors({
    origin: "*",
  })
);

app.listen(PORT, () => console.log("Server is running at port " + PORT));
