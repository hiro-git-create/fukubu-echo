// mathFormulas.js

// DuBois & DuBois BSA (m²) = 0.007184 * Height(cm)^0.725 * Weight(kg)^0.425
export function calc_bsa(inputs) {
  const { height, weight } = inputs;
  if (!height || !weight) return null;
  const bsa = 0.007184 * Math.pow(height, 0.725) * Math.pow(weight, 0.425);
  return { bsa: bsa.toFixed(2) };
}

// AVA (Continuity Equation) = (LVOTd/2)^2 * π * LVOT_VTI / AV_VTI
export function calc_ava(inputs) {
  const { lvot_d, lvot_vti, av_vti } = inputs;
  if (!lvot_d || !lvot_vti || !av_vti) return null;
  const lvot_area = Math.pow(lvot_d / 2, 2) * Math.PI;
  const ava = (lvot_area * lvot_vti) / av_vti;
  return { ava: ava.toFixed(2) };
}

// PISA EROA (cm²) = (2 * π * r^2 * Va) / Vmax
// Regurgitant Volume (mL) = EROA * VTI
export function calc_pisa(inputs) {
  const { radius, aliasing_vel, peak_vel, vti } = inputs;
  if (!radius || !aliasing_vel || !peak_vel) return null;
  const eroa = (2 * Math.PI * Math.pow(radius, 2) * aliasing_vel) / peak_vel;
  let result = { eroa: eroa.toFixed(2) };
  if (vti) {
    const rvol = eroa * vti;
    result.rvol = rvol.toFixed(1);
  }
  return result;
}

// Simplified Bernoulli PG (mmHg) = 4 * V^2
export function calc_pg(inputs) {
  const { velocity } = inputs;
  if (!velocity) return null;
  const pg = 4 * Math.pow(velocity, 2);
  return { pg: pg.toFixed(1) };
}

export const formulaRegistry = {
  calc_bsa,
  calc_ava,
  calc_pisa,
  calc_pg
};
