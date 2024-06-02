import './App.css';
import Clicks from './components/Clicks';
import Header from './components/Header';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Campaigns from './components/Campaigns';
import Offers from './components/Offers';
import OfferDetail from './components/OfferDetail';
import LeadsList from './components/LeadsList';
import StatisticElements from './components/StatisticElements';
import ClickPerDay from './components/statistic/clickPerDay';
import ClickPerInterestLevel from './components/statistic/clickPerInterestLevel';
import ClickPerOffer from './components/statistic/clickPerOffer';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/campaigns/offers/' element={<Offers />} />
          <Route path='/campaigns/offers/:offerSlug' element={<OfferDetail />} />
          <Route path='/campaigns' element={<Campaigns />} />
          <Route path='/leads' element={<LeadsList />} />
          <Route path='/clicks' element={<Clicks />} />
          <Route path='/statistic' element={<StatisticElements />} />
          <Route path='/click-per-day' element={<ClickPerDay />} />
          <Route path='/click-interest' element={<ClickPerInterestLevel />} />
          <Route path='/click-offers' element={<ClickPerOffer />} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}
export default App;