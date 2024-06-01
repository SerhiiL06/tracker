import './App.css';
import Clicks from './components/Clicks';
import Header from './components/Header';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Campaigns from './components/Campaigns';
import Offers from './components/Offers';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/campaigns/offers/' element={<Offers />} />
          <Route path='/campaigns' element={<Campaigns />} />

          <Route path='/clicks' element={<Clicks />} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}
export default App;