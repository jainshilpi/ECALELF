#include "Stats.hh"

stats::stats(const std::vector<float>& v):
	_isSorted(false),
	_sum(0.),
	_sum2(0.),
	_n(0)
{
	for(auto & val : v) {
		add(val);
	}
	std::sort(_values.begin(), _values.end());
	_isSorted = true;
}

void stats::add(const double val)
{
	_values.push_back(val);
	++_n;
	_sum += val;
	_sum2 += val * val;
}


float stats::eff_sigma(float q)
{
        if(!_isSorted) sort();
	if (_n < 2) return 0;
	size_t s = floor(q * _n);
	float d_min = _values[s] - _values[0];
	for (size_t i = s; i < _n; ++i) {
		float d = _values[i] - _values[i - s];
		if (d < d_min) d_min = d;
	}
	return d_min / 2.;
}


std::pair<size_t, size_t> stats::eff_sigma_indices(float q)
{
        if(!_isSorted) sort();
	if (_n < 2) return std::make_pair(0, 1);
	size_t s = floor(q * _n);
	float d_min = _values[s] - _values[0];
        size_t imin = 0, imax = 0;
	for (size_t i = s; i < _n; ++i) {
		float d = _values[i] - _values[i - s];
		if (d < d_min) {
                        d_min = d;
                        imin = i - s;
                        imax = i;
                }
	}
	return std::make_pair(imin, imax);
}


float stats::eff_mean(float q)
{
        std::pair<size_t, size_t> idx = eff_sigma_indices(q);
        double m = 0;
        for (size_t i = idx.first; i <= idx.second; ++i) m += _values[i];
        return m / (idx.second - idx.first + 1);
}


float stats::recursive_effective_mode(size_t imin, size_t imax, float q, float e)
{
	size_t n = imax - imin;
	if (imax == imin) return _values[imin]; // no element left
	else if (n == 1 || _values[imax] - _values[imin] < e) { // exit if 1 element left or distance < tolerance
		return 0.5 * (_values[imin] + _values[imax]);
	}
	size_t s = floor(q * n) - 1;
	float d_min = _values[imin + s] - _values[imin];
	size_t im = imin, iM = imin + s;
	for (size_t i = imin + s; i < imax; ++i) {
		float d = _values[i] - _values[i - s];
		if (d < d_min - e ) {
			d_min = d;
			im = i - s;
			iM = i;
		} else if (d - e < d_min) {
			iM = i;
		}
	}
	return recursive_effective_mode(im, iM, q, e);
}


void stats::fillHisto(TH1 * h)
{
        for (auto & v : _values) h->Fill(v);
}


std::ostream & operator<<(std::ostream& os, stats s)
{
	if(s.n() == 0) {
		os << s.name() << "\t" << s.n() << "\t" << "-" << "\t" << "-" << "\t" << "-" << "\t" << "-";
	} else {
		os << s.name() << "\t" << s.n() << "\t" << s.mean() << "\t" << s.stdDev() << "\t" << s.median() << "\t" << s.eff_sigma(); // << "\t" << s.recursive_effective_mode() ;
	}
	return os;
}