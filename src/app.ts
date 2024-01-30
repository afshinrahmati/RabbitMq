import * as express from "express";
import * as cors from "cors";
import { createConnection } from "typeorm";
const app = express();


createConnection().then(db => {
  app.use(cors({
    origin: ["http://localhost:3000", "http://localhost:8080", "http://localhost:4200"]
  }));

  app.use(express.json());

  app.listen(8000, () => {
    console.log("I can Start On port: 5210");
  });
});
