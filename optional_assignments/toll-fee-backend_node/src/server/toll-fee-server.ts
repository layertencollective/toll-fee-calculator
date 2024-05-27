import express, { Request, Response } from 'express';
const app = express();
const port = 3000;

app.use(express.json());

app.get('/ping', (_req: Request, res: Response) => {
  console.log('Alive!');
  res.status(200).send('...pong!');
});

app.get('/get-toll-fee', (req: Request, res: Response) => {
  const vehicle = req.query.vehicle;
  const passageDate = req.query.dateTime;
  console.log(`Getting toll fee for vehicle ${vehicle} at ${passageDate}`);

  res.status(200).send({ vehicle, passageDate, cost: 0 });
});

app.post('/get-all-fees-for-vehicle', (req: Request, res: Response) => {
  const vehicle = req.body.vehicle;
  const passageDates = req.body.passageDates;
  console.log(`Getting all toll fees for vehicle ${vehicle} at ${passageDates}`);

  res.status(200).send({ vehicle, passageDates, cost: 0 });
});

app.post('/get-all-fees-for-list', (req: Request, res: Response) => {
  const passages: { vehicle: string, date: any }[] = req.body.passages;
  let totalFee = 0;

  for (const passage of passages) {
    console.log(`Getting all toll fees for vehicle ${passage.vehicle} at ${passage.date}`);
    totalFee += 1;
  }

  res.status(200).send({ nrPassages: passages.length, totalFee});
});

export const start = () => {
  app.listen(port, () => {
    console.log(`Toll fee server listening at http://localhost:${port}`);
  });
}

export const Server = {
  start,
}