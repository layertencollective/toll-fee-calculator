import { FC, useState } from 'react';
import { Button, Grid, Paper, TextField } from '@mui/material';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { MobileDateTimePicker } from '@mui/x-date-pickers/MobileDateTimePicker';

type Passage = { vehicle?: string, dateTime: any};

export const TollCalculatorPage: FC = () => {
  const [_passages, setPassages] = useState<Passage[]>();
  const [vehicle, setVehicle] = useState<string>();
  const [dateTime, setDateTime] = useState<any>();

  const onDateTimePick = (value: any) => setDateTime(value);

  const addPassage = () => {
    setPassages((prevState) => [...(prevState || []), { vehicle, dateTime }])
  };

  return (
    <Paper elevation={3} style={{ padding: 24, maxWidth: '824px', minHeight: '480px' }}>
    <Grid container justifyContent='center' style={{ color: '#653545' }}>
      <Grid item>
        <h1>City Toll Fee Calculator</h1>
      </Grid>
      <Grid item>
        <h4>Enter vehicle, date and time to calculate cost!</h4>
      </Grid>
      <Grid container justifyContent='center' spacing={2}>
        <Grid item xs={12}>
          <TextField label='Vehicle type' variant='filled' onChange={(value) => setVehicle(value.target.value)} />
        </Grid>
        <Grid item xs={12}>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
          <MobileDateTimePicker ampm={false} onChange={onDateTimePick}/>
          </LocalizationProvider>
        </Grid>
        <Grid item xs={8}>
          <Button variant='outlined' onClick={addPassage}>Add!</Button>
        </Grid>
      </Grid>
      <Grid>
        <h3>Total cost: 0</h3>
      </Grid>
    </Grid>
    </Paper>
  )
}