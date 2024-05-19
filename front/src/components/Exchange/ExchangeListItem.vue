<template>
  <div class="exchange-bar row my-1">
    <div class="col-10 d-flex align-items-center">
      <div class="input-group">
        <span class="input-group-text">
          <select class="form-select">
            <option selected>통화</option>
            <option value="1">한국 (KRW)</option>
            <option value="2">일본 (JPY)</option>
            <option value="3">중국 (CNY)</option>
          </select></span
        >
        <input class="form-control" type="text" placeholder="값" />
      </div>
    </div>
    <div class="handle-box col-2">
      <button class="btn btn-secondary">
        <span class="material-symbols-outlined"> add </span>
      </button>
      <button class="btn btn-secondary mx-1">
        <span class="material-symbols-outlined"> remove </span>
      </button>
      <button class="btn btn-secondary"><span class="material-symbols-outlined"> menu </span></button>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.btn {
  padding: 10px;
  width: 40px;
  height: 40px;
}

.material-symbols-outlined {
  font-size: 20px;
}

.exchange-bar {
  height: 75px;
}

.handle-box {
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* .select-currency {
} */
</style>
