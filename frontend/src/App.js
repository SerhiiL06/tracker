import './App.css';
import Clicks from './components/clicks/Clicks';
import Header from './components/Header';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Campaigns from './components/campaigns/Campaigns';
import Offers from './components/offers/Offers';
import OfferDetail from './components/offers/OfferDetail';
import LeadsList from './components/leads/LeadsList';
import StatisticElements from './components/statistic/StatisticElements';
import ClickPerDay from './components/statistic/clickPerDay';
import ClickPerInterestLevel from './components/statistic/clickPerInterestLevel';
import ClickPerOffer from './components/statistic/clickPerOffer';
import Main from './components/Main';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path='/' element={<Main />} />
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